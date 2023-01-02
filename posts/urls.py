from django.urls import path, include
from posts import views

urlpatterns = [
    path('', views.create_post),
    # path('create/')
    # path('<int:pk>/', views.get_profile),
    # path('creation/', views.create_profile),
    # path('update/<int:pk>/', views.profile_management),
]