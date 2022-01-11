from django.shortcuts import render
from .models import Team

# Create your views here.
def home(req):
    teams = Team.objects.all()
    context = {
        'teams' : teams,
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

