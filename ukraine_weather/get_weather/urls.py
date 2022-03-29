from django.urls import path
from get_weather.views import api_weather

urlpatterns = [
    path('get', api_weather),
]
