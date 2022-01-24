from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('major/', views.major, name='major'),
    path('test/', views.test, name='test')
]