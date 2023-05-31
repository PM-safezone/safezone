from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.http import Http404, StreamingHttpResponse, HttpResponseServerError, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators import gzip
from django.contrib.auth.views import LoginView
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage, default_storage
from django.core.files.base import ContentFile
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
import base64
# Create your views here.
# @login_required
def main(request):
    #rtsp_url = 'rtsp://210.99.70.120:1935/live/cctv001.stream'
    #display_rtsp_video(rtsp_url)
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

    return render(request, 'upload_video.html', fileNo=video.fileNo)

def video(request):    
    return render(request, 'upload_video.html')

def video_analyze(request): 
    if request.method == 'POST':
        video_file = request.FILES['video_file']
        upload = default_storage.save(video_file.name,ContentFile(video_file.read()))

        command = 'python C:/Users/leeyo/Project/safezone/safezone/media/yolov5/detect.py --source C:/Users/leeyo/Project/safezone/safezone/media/' + video_file.name + ' --weights C:/Users/leeyo/Project/safezone/safezone/media/yolov5/runs/train/yolov5s_third/weights/best.pt --exist-ok'
        print(command)
        try:
            subprocess.run(command, shell=True, check=True)            
        except subprocess.CalledProcessError as e:
            print(e)

        detect_video_file = '/media/yolov5/runs/detect/exp/'+video_file.name
        detect_txt_file = 'C:/Users/leeyo/Project/safezone/safezone' + detect_video_file.split('.mp4')[0] + '.txt'
        f = open(detect_txt_file,'r')
        text_data = f.read()
        f.close()
        return render(request,'video_analyze.html',{'video_filename':detect_video_file,'text_data':text_data})
    return render(request, 'video_analyze.html')  


def video_detail(request, fileNo):
    video = get_object_or_404(Video, pk=fileNo)
    return render(request, 'video_detail.html', {'video': video})

def yolov5_webcam(request):
    return render(request, 'yolov5_webcam.html')

@csrf_exempt
def run_yolov5_webcam(request):
    if request.method == 'POST':
        
        #command = '/Users/seoyoobin/Desktop/MLP_AI Engineer Camp/safezone/safezone/safezone_app/yolov5/best.pt'
        command = 'python C:/Users/Jinsan/Desktop/safezone_project/safezone/safezone_app/yolov5/detect.py --weights C:/Users/Jinsan/Desktop/best.pt --save-txt --save-conf --conf-thres 0.60 --source 0'

        try:
            subprocess.run(command, shell=True, check=True)
            return HttpResponse("Detection completed successfully.")
        except subprocess.CalledProcessError as e:
            return HttpResponse(f"Error occurred while running detection: {e}")
        # 웹캠 캡처 객체 생성
        
        cap = cv2.VideoCapture(0)  # 0은 기본 웹캠을 나타냄
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


        # 웹캠 캡처 객체 해제
        cap.release()

        return render(request, 'run_yolov5_webcam.html')

    return JsonResponse({'message': '잘못된 요청입니다.'})


from .CCTV import VideoCamera, gen, video_feed

#def webcam_feed(request):
#    return StreamingHttpResponse(gen(IPWebCam()), content_type='multipart/x-mixed-replace; boundary=frame')


# --------------- 기능 테스트 진행중 -------------------- #
@gzip.gzip_page
def livefe(request):
    try:
        cam = VideoCamera()
        
        return StreamingHttpResponse(gen(cam))
    except:  # This is bad!
        pass

def find_camera(id):
    cameras = ['rtsp://210.99.70.120:1935/live/cctv001.stream',
    'rtsp://210.99.70.120:1935/live/cctv002.stream',
    'rtsp://210.99.70.120:1935/live/cctv003.stream',
    'rtsp://210.99.70.120:1935/live/cctv004.stream',
    'rtsp://210.99.70.120:1935/live/cctv005.stream',
    'rtsp://210.99.70.120:1935/live/cctv006.stream',
    'rtsp://210.99.70.120:1935/live/cctv007.stream',
    'rtsp://210.99.70.120:1935/live/cctv008.stream']
    return cameras[int(id)]


def gen_frames(camera_id):
     
    cam = find_camera(camera_id)
    cap=  cv2.VideoCapture(cam)
    
    while True:
        # for cap in caps:
        # # Capture frame-by-frame
        success, frame = cap.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result



def video_feed(request, id):
   
    """Video streaming route. Put this in the src attribute of an img tag."""
    return StreamingHttpResponse(gen_frames(id),
                    content_type='multipart/x-mixed-replace; boundary=frame')


def index():
    return render('main.html')


