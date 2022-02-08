from django.shortcuts import render, redirect
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import threading
from .models import QuestionChar
from django.utils import timezone
from django.contrib.auth import authenticate, login
from audiotest.forms import UserForm


# Create your views here.
"""
난수 추출 문제 나오는 함수
"""
def get_post(request):
    insung_num = request.POST.get('insung_num', False)
    skill_num = request.POST.get('skill_num', False)
    level = request.POST.get('level', False)
    insung_num = int(insung_num)
    skill_num = int(skill_num)
    question_list = QuestionChar.objects.filter(question_cla=0, question_dif=0).order_by('?')[0:insung_num]
    question_list1 = QuestionChar.objects.filter(question_cla=1, question_dif=level).order_by('?')[0:skill_num]
    context = {'question_list': question_list,
               'question_list1': question_list1}
    return render(request, 'interview_main.html', context)

def signup(request):
    """
    계정생성
    """
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'signup.html', {'form': form})

"""
비밀번호 출력
"""

"""
모의면접 화면 출력
"""
def index(request):
    return render(request, 'index.html')

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@gzip.gzip_page
def detectme(request):
    try:
        cam = VideoCamera()
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:  # This is bad! replace it with proper handling
        print("에러입니다...")
        pass

def interview(request):
    return render(request, 'interview.html')

def interview_question_setting(request):
    return render(request, 'interview_question_setting.html')

def interview_main(request):
    return render(request, 'interview_main.html')

def mypage(request):
    return render(request, 'mypage.html')

def mypage_privacy(request):
    return render(request, 'mypage_privacy.html')

def mypage_history(request):
    return render(request, 'mypage_history.html')

def base(request):
    return render(request, 'base.html')
