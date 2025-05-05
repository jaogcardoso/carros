from django.shortcuts import render
from cars.models import Car

# Create your views here.

def cars_view(request):
    search = request.GET.get('search')

    cars = Car.objects.all()
    print(cars)

    return render(request, 'cars.html', {'cars': cars })