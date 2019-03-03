from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index'),

path('getmeeting/', views.getmeeting, name='getmeeting'),
path('resources/', views.resources, name='resources'),
path('meetingDetail/<int:id>', views.meetingDetail, name='meetingDetail'),
path('newResource/', views.newResource, name='newResource'),
path('newMeeting/', views.newMeeting, name='newMeeting'),
path('loginmessage', views.loginmessage, name='Welcome'),
path('logoutmessage', views.logoutmessage, name='logoutMessage'),
 
]