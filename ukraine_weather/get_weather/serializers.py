from rest_framework import serializers

from get_weather.models import WeatherNow, City


class WeatherNowSerializer(serializers.ModelSerializer):
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


class CitySerializer(serializers.ModelSerializer):
    city = serializers.CharField(source="name")

    class Meta:
        model = City
        fields = ("city",)

    def validate(self, data):
        print(f"#### city Data before validation: {data}")
        validated_data = super().validate(data)
        print(f"#### city Data after validation: {validated_data}")
        cit = validated_data.get("city")
        try:
            City.objects.get(name=cit)
        except City.DoesNotExist:
            print(f"{cit} DoesNotExist in db")
        else:
            raise serializers.ValidationError(
                {"error": f"{cit} already exists in db"}
            )
        return validated_data
