from requests import get
from datetime import datetime

from get_weather.models import WeatherNow
from constants import (
    S_CITY,
    APPID,
    LINK,
    COUNTRY,
    RESPONSE,
    RES,
)

try:
    s_city = [i + ',' + COUNTRY for i in S_CITY]
    now = datetime.now()
    for city in s_city:
        res = get(LINK, params={'q': city, 'type': 'like',
                                'units': 'metric',
                                'APPID': APPID})
        RESPONSE.append(res)
    for r in RESPONSE:
        data = r.json()
        for i in data['list']:
            RES.append(WeatherNow(name=i['name'],
                                  date_time=now.strftime(
                                      "%d/%m/%Y %H:%M:%S"),
                                  weather='{0:+3.0f}'.format(
                                      i['main']['temp']),
                                  descriptian=i['weather'][0][
                                      'description']))

    WeatherNow.objects.bulk_create(RES)
except Exception as e:
    print("Exception (find):", e)
    pass
