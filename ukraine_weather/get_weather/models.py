from django.db import models


class WeatherNow(models.Model):
    city = models.CharField(max_length=50)
    date_time = models.DateField(auto_now=True)
    weather = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
