from rest_framework import serializers

from get_weather.models import WeatherNow


class WeatherNowSerializer(serializers.ModelSerializer):
    city = serializers.CharField()
    date_time = serializers.CharField()
    weather = serializers.CharField()
    description = serializers.CharField()

    class Meta:
        model = WeatherNow
        fields = ("city", "date_time", "weather", "description")

    def validate(self, data):
        print(f"#### weather now Data before validation: {data}")
        validated_data = super().validate(data)
        print(f"#### weather now Data after validation: {data}")
        cit = validated_data.get("city")
        try:
            WeatherNow.objects.get(title=cit)
        except WeatherNow.DoesNotExist:
            print(f"weather of {cit} DoesNotExist")
        else:
            raise serializers.ValidationError(
                {"error": f"weather of {cit} already exists"}
            )
        return validated_data

