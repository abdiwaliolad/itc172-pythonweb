from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index'),

path('getmeeting/', views.getmeeting, name='getmeeting'),
path('resources/', views.resources, name='resources'),
path('meetingDetail/<int:id>', views.meetingDetail, name='meetingDetail'),
 
]