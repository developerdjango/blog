from django.urls import path
from mainApp import views
urlpatterns = [
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),

    path('', views.home, name='home'),

]
