import cv2
from django.shortcuts import render
#from safezone_app.models import Setting
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.http import Http404, StreamingHttpResponse, HttpResponseServerError, JsonResponse
from PIL import Image
import base64

def stream(request, setno):
    # RTSP 스트림을 가져오는 함수 호출
    get_frame_from_rtsp("rtsp://210.99.70.120:1935/live/cctv001.stream")
    setting = Setting.get_object_all(id = setno)
    # 가져온 이미지를 웹 페이지에 전달
    # 예: context 변수에 이미지 경로나 데이터를 추가하여 렌더링합니다.
    context = {
        'image_path': '/path/to/streaming/image.jpg'
    }
    return render(request, 'stream.html', context)


def play_rtsp_video(rtsp_url):
    video_capture = cv2.VideoCapture(rtsp_url)
    
    while True:
        ret, frame = video_capture.read()
        if not ret:
            break
        
        cv2.imshow('RTSP Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    video_capture.release()
    cv2.destroyAllWindows()

# RTSP 비디오 재생
rtsp_url = 'rtsp://210.99.70.120:1935/live/cctv001.stream'
play_rtsp_video(rtsp_url)


def display_rtsp_video(rtsp_url):
    video_capture = cv2.VideoCapture(rtsp_url)
    
    while True:
        ret, frame = video_capture.read()
        if not ret:
            break
        
        # 비디오 프레임을 <video> 태그에 표시
        ret, buffer = cv2.imencode('.jpg', frame)
        video_data = base64.b64encode(buffer)
        video_data_uri = 'data:image/jpeg;base64,' + video_data.decode('utf-8')
        
        # JavaScript를 사용하여 <video> 태그의 src를 업데이트
        js_code = f"document.getElementById('videoPlayer').src = '{video_data_uri}';"
        js_code += "document.getElementById('videoPlayer').play();"
        # js_code를 WebSocket 또는 Ajax를 통해 웹 페이지로 전송하거나, Django의 Template에 넘겨준 뒤 실행
        
        # 이미지를 <img> 태그에 표시
        ret, buffer = cv2.imencode('.jpg', frame)
        image_data = base64.b64encode(buffer)
        image_data_uri = 'data:image/jpeg;base64,' + image_data.decode('utf-8')
        
        # JavaScript를 사용하여 <img> 태그의 src를 업데이트
        js_code = f"document.getElementById('imageDisplay').src = '{image_data_uri}';"
        # js_code를 WebSocket 또는 Ajax를 통해 웹 페이지로 전송하거나, Django의 Template에 넘겨준 뒤 실행
    
    video_capture.release()