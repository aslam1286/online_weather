from django.shortcuts import render
import requests

def home(request):
    city=request.GET.get('city',"Pune")
    url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=945e9fe0b6e3f98a16909ba6873c15c8"
    data=requests.get(url).json()

    pload= {
        'city': data['name'],
        'weather': data['weather'][0]['main'],
        'icon': data['weather'][0]['icon'],
        'kelvin_temperature': data['main']['temp'],
        'celcius_temperature': int(data['main']['temp']-273),
        'pressure': data['main']['pressure'],
        'humidity': data['main']['humidity'],
        'description': data['weather'][0]['description'],
        }

    context={'data': pload}
    return render(request, 'home.html', context)