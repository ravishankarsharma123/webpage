from django.contrib import admin
from django.urls import path , include
from sspr import views

urlpatterns = [
path('', views.index,name='new'),
path('firstpage', views.firstpage,name='new'),
path('secondpage', views.secondpage,name='new'),
path('thirdpage', views.thirdpage,name='new'),
]
