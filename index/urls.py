from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('index/', views.index),
    path('about/', views.about),
    path('analyze/', views.analyze),
    path('automation/', views.automation),
    path('security/', views.security),
    path('course/', views.course),
]