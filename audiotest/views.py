from django.shortcuts import render, redirect
from django.utils import timezone
import datetime as dt
from .models import VideoSave
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import cv2
import threading
# Create your views here.

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

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0 + cv2.CAP_DSHOW)
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

cam = VideoCamera()

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
    except:
        print("에러입니다.")
        pass