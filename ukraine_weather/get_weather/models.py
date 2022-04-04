from django.db import models


class WeatherNow(models.Model):
    date_time = models.DateField(auto_now=True)
    weather = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    city = models.ForeignKey(
        "City",
        on_delete=models.CASCADE,
        related_name="weather",
    )


class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
