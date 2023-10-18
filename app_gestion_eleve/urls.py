from django.urls import path
from .import views

urlpatterns = [
    path('', views.index),
    path('modifier/', views.modifier, name="modifier"),
]
