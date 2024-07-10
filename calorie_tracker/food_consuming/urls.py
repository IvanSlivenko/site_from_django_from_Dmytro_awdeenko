from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('delete/<int:id>/', views.DeleteView.as_view(), name='delete'),
]