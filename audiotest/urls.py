from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('CVtest', views.detectme, name='detectme'),
    path('interview', views.interview, name='interview'),
    path('interview/setting', views.interview_question_setting, name='setting'),
    path('mypage', views.mypage, name='mypage'),
    path('mypage/privacy', views.mypage_privacy, name='privacy'),
    path('mypage/history', views.mypage_history, name='history'),
    path('interview/main', views.get_post, name='main'),
    path('base', views.base, name='base'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
