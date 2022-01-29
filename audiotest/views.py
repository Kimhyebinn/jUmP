from django.shortcuts import render, redirect
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import cv2
import threading
from django.utils import timezone

# Create your views here.
"""
모의면접 화면 출력
"""
def index(request):
    return render(request, 'index.html')

def interview(request):
    return render(request, 'interview.html')

def interview_setting(request):
    return render(request, 'interview_question_setting.html')

def interview_main(request):
    return render(request, 'interview_main.html')

def mypage(request):
    return render(request, 'mypage.html')

def mypage_privacy(request):
    return render(request, 'mypage_privacy.html')

def mypage_history(request):
    return render(request, 'mypage_history.html')

