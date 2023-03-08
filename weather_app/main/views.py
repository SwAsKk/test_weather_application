from django.shortcuts import render
import requests


def index(request):
    context = {}
    api_key = 'MTRhNTIwOWQtYjBhMS00Nzc0LWJkZTktMzZmNjBhODk3NzA0'
    location = 'Moscow'
    url = f'https://api.m3o.com/v1/weather/Now?location={location}'
    headers = {'Authorization': f'Bearer {api_key}'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        print(f"Current temperature in {location}: {data['temp_c']}°C")
        context['temp_c'] = data['temp_c']
        print(context['temp_c'])
    else:
        print(f"Error: {response.status_code}")
    
    return render(request, 'index.html', context)