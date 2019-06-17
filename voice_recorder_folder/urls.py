"""voice_recorder_folder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from voice_recorder import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/', views.welcomeApi, name='welcome'),
    path('api/record/start', views.uploadAudio, name='upload-audio'),
    path('api/record/stop', views.stop_audio, name='stop-audio'),
    path('api/record/library/start', views.start_audio_library, name='upload_library_audio'),
    path('api/record/library/stop', views.stop_record_library, name='stop_library_audio')
]
