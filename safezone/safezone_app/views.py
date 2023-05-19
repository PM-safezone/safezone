from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.http import Http404
from django.utils.decorators import method_decorator

from .forms import VideoForm
from .models import Video
from django.contrib.auth.views import LoginView
from account_app.decorators import admin_ownership_required
from account_app.views import has_ownership

# Create your views here.
@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
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
    else:
        form = VideoForm()                                          # POST 아니면 화면 다시 띄우기

    return render(request, 'upload_video.html', {'form': form})

def video_detail(request, fileNo):
    video = get_object_or_404(Video, pk=fileNo)
    return render(request, 'video_detail.html', {'video': video})