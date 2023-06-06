from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_page, name='main'),
    path('achievement/<int:achievement_id>', views.achievement_page),
    path('service/<int:service_id>', views.service_page),
]