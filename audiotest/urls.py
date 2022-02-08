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
<<<<<<< HEAD
    path('base', views.base, name='base'),
=======
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('signup', views.signup, name='signup'),
>>>>>>> 4ddd7f84fcad739465ca76ea8c8b2fd603738920
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
