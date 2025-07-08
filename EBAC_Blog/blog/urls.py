from django.urls import path

from blog import views

urlspatters = [
    path('', views.PostView.as_view(), name='home')
]