import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    url = 'http://api.weatherapi.com/v1/current.json?key=b56f1ac1bf174fb4814151817241402&q={}'

    if request.method == 'POST':
        form=CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    weather_cities = []

    for city in cities:
        

        r = requests.get(url.format(city.name)).json()

        city_weather = {
            'city' :  city.name ,
            'temperature': r["current"]["temp_c"] ,
            'description': r["current"]["condition"]["text"] ,
            'icon': r["current"]["condition"]["icon"]  , 
            'wind': r["current"]["wind_kph"],
            'humidity':r["current"]["humidity"] ,                      
        }
        
        weather_cities.append(city_weather)
    
    print(weather_cities)  

    context = {'weather_cities':weather_cities, 'form':form }
    return render(request,'app/main.html',context)

def delete_city(request, city_name):
    if request.method == 'POST':
        City.objects.filter(name=city_name).delete()
        # Şehir başarıyla silindikten sonra ana sayfaya yönlendir
        return HttpResponseRedirect('/')