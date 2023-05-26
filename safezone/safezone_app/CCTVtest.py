import cv2
from django.shortcuts import render
#from safezone_app.models import Setting
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.http import Http404, StreamingHttpResponse, HttpResponseServerError, JsonResponse
from PIL import Image
import base64

#def stream(request, setno):
#    # RTSP 스트림을 가져오는 함수 호출
#    get_frame_from_rtsp("rtsp://210.99.70.120:1935/live/cctv001.stream")
#    setting = Setting.get_object_all(id = setno)
#    # 가져온 이미지를 웹 페이지에 전달
#    # 예: context 변수에 이미지 경로나 데이터를 추가하여 렌더링합니다.
#    context = {
#        'image_path': '/path/to/streaming/image.jpg'
#    }
#    return render(request, 'stream.html', context)


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


def display_rtsp_video(rtsp_url, frame_interval=10):
    video_capture = cv2.VideoCapture(rtsp_url)
    frame_counter = 0
    
    while True:
        ret, frame = video_capture.read()
        if not ret:
            break
        
        frame_counter += 1
        if frame_counter % frame_interval != 0:
            continue
        
        # 비디오 프레임을 <video> 태그에 표시
        ret, buffer = cv2.imencode('.jpg', frame)
        video_data = base64.b64encode(buffer)
        video_data_uri = 'data:image/jpeg;base64,' + video_data.decode('utf-8')
        
        # JavaScript를 사용하여 <video> 태그의 src를 업데이트
        js_code = f"document.getElementById('videoPlayer').src = '{video_data_uri}';"
        js_code += "document.getElementById('videoPlayer').play();"
        # js_code를 WebSocket 또는 Ajax를 통해 웹 페이지로 전송하거나, Django의 Template에 넘겨준 뒤 실행
        
    video_capture.release()
    

import ffmpeg
import numpy as np
import cv2


def main(source):
    args = {"rtsp_transport": "tcp"}    # 添加参数
    probe = ffmpeg.probe(source)
    cap_info = next(x for x in probe['streams'] if x['codec_type'] == 'video')
    print("fps: {}".format(cap_info['r_frame_rate']))
    width = cap_info['width']           # 获取视频流的宽度
    height = cap_info['height']         # 获取视频流的高度
    up, down = str(cap_info['r_frame_rate']).split('/')
    fps = eval(up) / eval(down)
    print("fps: {}".format(fps))    # 读取可能会出错错误
    process1 = (
        ffmpeg
        .input(source, fflags='nobuffer',flags='low_delay')
        .output('pipe:', format='rawvideo', pix_fmt='rgb24')
        .overwrite_output()
        .run_async(pipe_stdout=True)
    )
    while True:
        in_bytes = process1.stdout.read(width * height * 3)     # 读取图片
        if not in_bytes:
            break
        # 转成ndarray
        in_frame = (
            np
            .frombuffer(in_bytes, np.uint8)
            .reshape([height, width, 3])
        )
        frame = cv2.resize(in_frame, (1280, 720))   # 改变图片尺寸
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)  # 转成BGR
        cv2.imshow("ffmpeg", frame)
        if cv2.waitKey(1) == ord('q'):
            break
    process1.kill()             # 关闭


if __name__ == "__main__":
    source = "rtsp://210.99.70.120:1935/live/cctv001.stream"
    main(source)