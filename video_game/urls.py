from django.urls import path, include
from video_game import views

urlpatterns = [
    path('add/', views.add_video_game),
]