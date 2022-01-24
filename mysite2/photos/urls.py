from django.urls import path
from . import views


app_name= 'photos'

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('photo/<str:pk>/', views.photo, name='photo'),
]