from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from get_weather.models import WeatherNow
from get_weather.serializers import WeatherNowSerializer, CitySerializer


@api_view(["GET"])
def api_weather(request, city):
    if request.method == "GET":
        w = WeatherNow.objects.all()
        serializer = WeatherNowSerializer(w, many=True)
        return Response(serializer.data)


@api_view(["POST"])
def api_city(request):
    if request.method == "POST":
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

