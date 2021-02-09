from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('request/',views.mainview,name='request'),
    path('result/',views.unknown,name='my_function'),
]
