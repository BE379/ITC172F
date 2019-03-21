from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('student/', views.getstudent, name='getstudent'),
    path('classes/', views.getclasses, name='getclasses'),
    path('schedule/', views.getschedule, name='getschedule'),
    path('classdetail/<int:id>', views.getclassdetail, name='getclassdetail'),
    path('newClass/', views.newClass, name='newclass'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]