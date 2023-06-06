from django.shortcuts import render, get_object_or_404
from .models import Portfolio
import datetime

# Create your views here.


def main_page(request):
    services = Portfolio.objects.filter(category='cat').order_by('-id')
    achievements = Portfolio.objects.filter(category="cat2").order_by('-id')
    return render(request, 'portfolio/home.html', {"services": services, "achievements": achievements})


def achievement_page(request, achievement_id):
    achievement = get_object_or_404(Portfolio, pk=achievement_id)
    return render(request, 'portfolio/achievement.html', {"achievement": achievement})


def service_page(request, service_id):
    service = get_object_or_404(Portfolio, pk=service_id)
    return render(request, 'portfolio/service.html', {"service": service})