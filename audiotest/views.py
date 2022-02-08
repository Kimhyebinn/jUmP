from django.shortcuts import render, redirect
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

"""
비밀번호 출력
"""

def index(request):
    return render(request, 'index.html')

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
