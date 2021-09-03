from django.shortcuts import render
from .models import Teams
from cars.models import Car

# Create your views here.
def home(request):
    team = Teams.objects.all()
    featured_car = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_car = Car.objects.order_by(('-created_date'))
    data = {
        'team' : team,
        'featured_car' : featured_car,
        'all_car' : all_car
    }
    return render(request, 'pages/home.html', data)



def about(request):
    team = Teams.objects.all()
    data = {
        'team' : team
    }
    return render(request, 'pages/about.html', data)


def services(request):
    return render(request, 'pages/services.html')


def contact(request):
    return render(request, 'pages/contact.html')


