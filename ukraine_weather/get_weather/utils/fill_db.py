from requests import get
from datetime import datetime

from get_weather.models import WeatherNow, City
from get_weather.utils.constants import (
    APPID,
    LINK,
    COUNTRY,
    RES,
    LAST_NAME
)


def main():
    global LAST_NAME
    try:
        now = datetime.now()
        for city in City.objects.all():                                         # перебираем все города
            c = f"{city.name}, {COUNTRY}"                                       # превращаем название городов в нужный формат для запроса
            p = {'q': c, 'type': 'like', 'units': 'metric', 'APPID': APPID}     # для запроса
            res = get(LINK, params=p).json()                                    # сам запрос
            for i in res['list']:
                if i['name'] != LAST_NAME:
                    print(f"i['name'] - {i['name']}")
                    print(f"RES is {type(RES)}")
                    RES.append(WeatherNow(date_time=now.strftime("%d/%m/%Y %H:%M:%S"),
                               weather='{0:+3.0f}'.format(i['main']['temp']),
                               description=i['weather'][0]['description']),
                               city=city)
                    LAST_NAME = i['name']

        WeatherNow.objects.bulk_create(RES)
    except Exception as e:
        print("Exception (find):", e)
        pass


main()
