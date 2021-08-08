from django.contrib import admin
from django.urls import path
from . import views

app_name = 'ytproject'


urlpatterns = [
    path('', views.index , name = 'home'),
    path('download/', views.download , name = 'download'),
    path('download/<itag>', views.yt_download_done , name = 'download_done'),
    path('download/<itag>', views.yt_mp3download_done , name = 'mp3download_done')
]
