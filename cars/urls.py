from django.urls import path
from cars import views
urlpatterns = [
    path('car/', views.car, name='car'),
    path('<int:id>', views.car_detail, name='car_detail'),
]
