from django.shortcuts import render

# Create your views here.


def car_home(req):
    return render(req, 'cars/cars.html')