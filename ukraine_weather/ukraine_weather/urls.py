from django.urls import path
from django.urls import include

urlpatterns = [
    path('weather/', include("get_weather.urls")),
]
