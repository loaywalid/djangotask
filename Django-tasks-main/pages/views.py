from django.shortcuts import render
from django.http import HttpResponse
from .models import Car 

# Create your views here.

def viewCars(request):
       return render(request,'pages/cars.html', {"cars":Car.objects.all().order_by('model').exclude(name="lancer")})
 
def task1(request):
    newdic =[{"user":"loay","age":23,"salary":5000},{"user":"ahmed","age":26,"salary":6000},{"user":"amr","age":27,"salary":7000}]
    dic = {"users" : newdic}
    return render(request,'pages/task1.html',dic)