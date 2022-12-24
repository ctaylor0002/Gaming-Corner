from django.urls import path, include
from user_collection import views

urlpatterns = [
    path('<int:user_id>/', views.user_collection),
]