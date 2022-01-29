from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import include

urlpatterns = [
    path('', views.index, name='index'),
    path('interview', views.interview, name='interview'),
    path('interview/setting', views.interview_setting, name='setting'),
    path('interview/main', views.interview_main, name='main'),
    path('mypage', views.mypage, name='mypage'),
    path('mypage/privacy', views.mypage_privacy, name='privacy'),
    path('mypage/history', views.mypage_history, name='history'),
]