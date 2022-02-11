from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

app_name = "audiotest"

urlpatterns = [
    path('', views.index, name='index'),
    path('interview', views.interview, name='interview'),
    path('interview/setting', views.interview_question_setting, name='setting'),
    path('mypage/privacy', views.mypage_privacy, name='privacy'),
    path('interview/main', views.get_post, name='main'),
    path('change_password/', views.change_password, name="re_password"),
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
