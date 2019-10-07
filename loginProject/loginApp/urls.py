from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('in-class/', views.inclass, name='inclass'),
    path('login/', views.login, name='login'),
]