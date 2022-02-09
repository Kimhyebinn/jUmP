from django.shortcuts import render, redirect
import threading
from .models import QuestionChar
from django.utils import timezone
from audiotest.forms import UserForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash, authenticate, login
from django.contrib.auth.hashers import check_password
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib import messages
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

"""
비밀번호 변경
"""
def change_password(request):
  if request.method == "POST":
    user = request.user
    origin_password = request.POST["origin_password"]
    if check_password(origin_password, user.password):
      new_password = request.POST["new_password"]
      confirm_password = request.POST["confirm_password"]
      if new_password == confirm_password:
        user.set_password(new_password)
        user.save()
        auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        messages.error(request, '비밀번호가 변경되었습니다.')
        return redirect('privacy')
      else:
        messages.error(request, '변경할 비밀번호와 확인이 일치하지 않습니다.')
    else:
      messages.error(request, '현재 비밀번호가 일치하지 않습니다.')
    return render(request, 'mypage_privacy.html')
  else:
    return render(request, 'mypage_privacy.html')

"""
모의면접 화면 출력
"""

def index(request):
    return render(request, 'index.html')

def index1(request):
    return render(request, 'index1.html')

def interview(request):
    return render(request, 'interview.html')

def interview_question_setting(request):
    return render(request, 'interview_question_setting.html')

def interview_main(request):
    return render(request, 'interview_main.html')

def mypage(request):
    return render(request, 'mypage.html')

def mypage_privacy(request):
    cur_user = request.user
    if cur_user.is_authenticated:
        user = User.objects.get(username=request.user)

        return render(request, 'mypage_privacy.html', {'user': user})
    else:
     return redirect('index1')

def base(request):

    return render(request, 'base.html')


