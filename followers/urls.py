from django.urls import path, include
from followers import views

urlpatterns = [
    path('', views.following),
    path('list/', views.followers),
    
]