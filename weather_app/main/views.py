from django.shortcuts import render
import requests


def index(request):
    context = {}
    api_key = 'foobar'
    location = 'Moscow'
    url = f'https://api.m3o.com/v1/weather/Now?location={location}'
    headers = {'Authorization': f'Bearer {api_key}'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        context['weather_now'] = data
    else:
        print(f"Error: {response.status_code}")
    
    return render(request, 'index.html', context)

def forecast(request):
    context = {}
    api_key = 'foobar'
    location = 'Moscow'
    url = f'https://api.m3o.com/v1/weather/forecast?location={location}&days=10'
    headers = {'Authorization': f'Bearer {api_key}'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        print(data)
        context['forecast'] = data
    else:
        print(f"Error: {response.status_code}")

    return render(request,'forecast.html', context)