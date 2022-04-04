from django.urls import path
from get_weather.views import api_weather, api_city

urlpatterns = [
    path('get/<str:city>', api_weather),
    path('post/', api_city),
]
