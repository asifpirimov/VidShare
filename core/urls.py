from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('upload/', views.upload_video, name='upload_video'),
    path('my-videos/', views.my_videos_list, name='my_videos_list'),
    path('my-videos/<int:video_id>/', views.my_video_detail, name='my_video_detail'),
    path('profile/', views.profile, name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
