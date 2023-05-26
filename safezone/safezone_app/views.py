from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.http import Http404, StreamingHttpResponse, HttpResponseServerError, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators import gzip
from django.contrib.auth.views import LoginView
from django.views.decorators.csrf import csrf_exempt
from account_app.decorators import admin_ownership_required
import cv2
import os
from torchvision import transforms
from PIL import Image
import time
from .forms import VideoForm
from .models import Video
from yolov5.models.experimental import *
import subprocess
import json
from collections import deque

# Create your views here.
# @login_required
def main(request):
    return render(request, 'main.html')

def settings(request):
    if request.method == 'POST':
        log_interval = request.POST.get('log-interval')
        log_location = request.POST.get('log-location')
        video_location = request.POST.get('video-location')
        
        # 데이터 처리 및 저장 로직 작성
        # 기존 설정이 있는지 확인합니다.
        settings = get_object_or_404(Video, title='settings')
        
        # 기존 설정이 없으면 새로운 객체를 생성합니다.
        if not settings:
            settings = Video(title='settings')
        
        # 새로운 설정값을 업데이트합니다.
        settings.log_interval = log_interval
        settings.log_location = log_location
        settings.video_location = video_location
        
        # 설정을 저장합니다.
        settings.save()
        
        return HttpResponse('Settings updated successfully!')
    
    return render(request, 'settings.html')
    
# account_app 에서 대체
# class CustomLoginView(LoginView):
#     template_name = 'testpage.html'
#     authentication_form = LoginForm
    
# def login(request):
#     return render(request, 'testpage.html')



def upload_video(request):
    if request.method == 'POST':                            # form 으로 Method=POST 로 받아와서 작업
        form = VideoForm(request.POST, request.FILES)       # forms.py 에서 작업하기위해 POST 로 요청, FILES 를 불러옴 
        if form.is_valid():                                 # form 의 title, video_file 형식으로 들어오는지 유효성 검사
            
            video_file = request.FILES.get('video_file')    # <label for="video_file">Title:</label>
            video_name = video_file.name                    # <input type="file" class="form-control-file" id="video_file" name="video_file">
                                                            # 에서 받아온 video_file 을 get files 화
            video = form.save(commit=False)                 # file 들어온 값들을 form.save 적용은 안하고 video 에 입력
            
            video.title = video_name                        # video_name 을 title 에 입력
            video.filepath = 'videos/' + video_name         # 'videos/' + video_name 으로 파일 경로 입력
            video.video_file = 'videos/' + video_name
            
            video.save()                                    # DB 적용 video 의 값을

            return redirect('video_detail', fileNo=video.fileNo)    # DB 적용이 완료되면 video_detail 을 불러와, video_detail/fileNo
                                                                    # 으로 redirect
        else:
            print(form.errors)                                      # 유효성 검사 틀리면 프린트
    if request.method == 'POST':                            # form 으로 Method=POST 로 받아와서 작업
        form = VideoForm(request.POST, request.FILES)       # forms.py 에서 작업하기위해 POST 로 요청, FILES 를 불러옴
        if form.is_valid():                                 # form 의 title, video_file 형식으로 들어오는지 유효성 검사

            video_file = request.FILES.get('video_file')    # <label for="video_file">Title:</label>
            video_name = video_file.name                    # <input type="file" class="form-control-file" id="video_file" name="video_file">
                                                            # 에서 받아온 video_file 을 get files 화
            video = form.save(commit=False)                 # file 들어온 값들을 form.save 적용은 안하고 video 에 입력

            video.title = video_name                        # video_name 을 title 에 입력
            video.filepath = 'videos/' + video_name         # 'videos/' + video_name 으로 파일 경로 입력
            video.video_file = 'videos/' + video_name

            video.save()                                    # DB 적용 video 의 값을

            return redirect('video_detail', fileNo=video.fileNo)    # DB 적용이 완료되면 video_detail 을 불러와, video_detail/fileNo
                                                                    # 으로 redirect
        else:
            print(form.errors)                                      # 유효성 검사 틀리면 프린트
    else:
        form = VideoForm()                                          # POST 아니면 화면 다시 띄우기

    return render(request, 'upload_video.html', {'form': form})

def video_detail(request, fileNo):
    video = get_object_or_404(Video, pk=fileNo)
def video_detail(request, fileNo):
    video = get_object_or_404(Video, pk=fileNo)
    return render(request, 'video_detail.html', {'video': video})

def yolov5_webcam(request):
    return render(request, 'yolov5_webcam.html')

@csrf_exempt
def run_yolov5_webcam(request):
    if request.method == 'POST':
        
        command = 'python D:\Project_by_me\safezone\safezone\safezone_app\yolov5\detect.py --weights D:\Project_by_me\model\best.pt --save-txt --save-conf --conf-thres 0.60 --source 0'
        try:
            subprocess.run(command, shell=True, check=True)
            return HttpResponse("Detection completed successfully.")
        except subprocess.CalledProcessError as e:
            return HttpResponse(f"Error occurred while running detection: {e}")
        # 웹캠 캡처 객체 생성
        cap = cv2.VideoCapture(0)  # 0 은 기본 웹캠을 나타냄
        #count = count * 30
        #start_file_number = count
        #end_file_number = count + 299

        # detect.py 스크립트 실행
        os.system(command)

        # 일정 시간마다 출력 결과 확인
        
            # 특정 클래스 객체 검출 수 확인
        
        
        # detect.py 실행을 중지하는지 확인
        if 'stop_flag' in request.POST and request.POST['stop_flag'] == 'true':
            # 웹캠 캡처 객체 해제
            cap.release()
            return JsonResponse({'message': '감지를 중지했습니다.'})

        # Subprocess 종료 대기
        #process.communicate()

        # 웹캠 캡처 객체 해제
        cap.release()

        return render(request, 'run_yolov5_webcam.html')

    return JsonResponse({'message': '잘못된 요청입니다.'})
#class VideoCamera(object):
#
#    def __init__(self):
#        self.video = cv2.VideoCapture(0)
#        self.video.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
#        self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)
#        (self.grabbed, self.frame) = self.video.read()
#
#
#        # Yolov5m model load
#        self.model = torch.hub.load('ultralytics/yolov5', 'custom', path='safezone_app/best.pt', force_reload=True)
#        self.model.eval()
#
#        threading.Thread(target=self.update, args=()).start()
#
#    def __del__(self):
#        self.video.release()
#
#    def get_frame(self):
#        image = self.frame
#        _, jpeg = cv2.imencode('.jpg', image)
#        return jpeg.tobytes()
#
#    def update(self):
#        while True:
#            (self.grabbed, self.frame) = self.video.read()
#
#            # 이미지 전처리
#            image_pil = Image.fromarray(cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB))  # OpenCV 이미지를 PIL 이미지로 변환
#
#            transform = transforms.Compose([
#                transforms.Resize((224, 224)),
#                transforms.ToTensor(),
#                transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
#            ])
#            image = transform(image_pil)
#            image = image.unsqueeze(0)
#
#            # 추론 수행
#            results = self.model(image)
#            boxes = results[0, :, :4].detach().cpu().numpy()  # 경계 상자 좌표 추출
#            confidences = results[0, :, 4].detach().cpu().numpy()  # 객체의 신뢰도 점수 추출
#            class_labels = results[0, :, 5].detach().cpu().numpy()  # 클래스 레이블 추출
#
#            predictions = []
#            # 경계 상자와 클래스 레이블을 웹캠 화면에 표시
#            for box, confidence, class_label in zip(boxes, confidences, class_labels):
#                x1, y1, x2, y2 = map(int, box)  # 경계 상자 좌표 추출
#
#                # 경계 상자 그리기
#                cv2.rectangle(self.frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
#
#                # 클래스 레이블과 신뢰도 점수 표시
#                text = f'{class_label}: {confidence:.2f}'
#                cv2.putText(self.frame, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
#
#                predictions.append({
#                    'class_label': class_label,
#                    'confidence': confidence.item()
#                })
#            # 결과를 JSON 형식으로 반환
#            output = {'predictions': predictions}
#
#            # JSON 응답을 처리하기 위해 JsonResponse 사용
#            return JsonResponse(output)
#
#
#
#def gen(camera):
#    while True:
#        frame = camera.get_frame()
#        yield(b'--frame\r\n'
#              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
#
#@csrf_exempt
#def livefeed(request):
#    try:
#        cam = VideoCamera()
#        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
#    except Exception as e:
#        print(e)
#        return HttpResponseServerError()
    

