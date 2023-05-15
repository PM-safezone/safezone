from django.shortcuts import render, redirect
from .forms import VideoForm
from .models import Video

# Create your views here.
def main(request):
    return render()

def setting(request, memberid):
    # member = Member.object
    return render()
    


def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save()  # 업로드된 비디오 저장
            # video 경로를 DB에 저장하거나 필요한 로직 수행
            return redirect('video_detail', video_id=video.id)
    else:
        form = VideoForm()
    return render(request, 'upload_video.html', {'form': form})

def video_detail(request, video_id):
    video = Video.objects.get(id=video_id)
    return render(request, 'video_detail.html', {'video': video})