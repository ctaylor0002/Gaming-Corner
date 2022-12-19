from django.urls import path, include
from user_profile import views

urlpatterns = [
    path('creation/', views.create_profile),
]