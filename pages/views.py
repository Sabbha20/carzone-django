from django.shortcuts import render
from .models import Team
from cars.models import Cars

# Create your views here.
def home(req):
    teams = Team.objects.all()
    featured_cars = Cars.objects.all().order_by('-created_date').filter(is_featured=True)
    cars = Cars.objects.all().order_by('-created_date')
    context = {
        'teams' : teams,
        'featured_cars': featured_cars,
        'cars': cars,
    }
    return render(req, 'pages/home.html', context)

def about(req):
    teams = Team.objects.all()
    context = {
        'teams' : teams,
        'bannertitle': 'About Us',
    }
    return render(req, 'pages/about.html', context)

def services(req):
    return render(req, 'pages/services.html', {'bannertitle': 'Services'})

def contact(req):
    return render(req, 'pages/contact.html', {'bannertitle': 'Contact Us'})

