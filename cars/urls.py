from django.urls import path
from . import views

urlpatterns = [
    path('', views.car_home, name='car_home'),
]
