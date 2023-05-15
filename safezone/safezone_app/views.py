from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .forms import VideoForm
from .models import Video

# Create your views here.
def main(request):
    return render()

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
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video_file = request.FILES.get('video-file')
            video = form.save()  # 업로드된 비디오 저장
            # video 경로를 DB에 저장하거나 필요한 로직 수행
            return redirect('video_detail', video_id=video.id)
    else:
        form = VideoForm()
    return render(request, 'upload_video.html', {'form': form})

def video_detail(request, video_id):
    video = Video.objects.get(id=video_id)
    return render(request, 'video_detail.html', {'video': video})