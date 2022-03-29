from requests import get
from datetime import datetime

from get_weather.models import WeatherNow
from get_weather.utils.constants import (
    S_CITY,
    APPID,
    LINK,
    COUNTRY,
    RESPONSE,
    RES,
    LAST_NAME,
)


def main():
    global LAST_NAME
    try:
        s_city = [i + ',' + COUNTRY for i in S_CITY]
        now = datetime.now()
        for city in s_city:
            p = {'q': city, 'type': 'like', 'units': 'metric', 'APPID': APPID}
            res = get(LINK, params=p)
            # print(f'for request {LINK}: {p}\n{res}')
            RESPONSE.append(res)
        for r in RESPONSE:
            data = r.json()
            for i in data['list']:
                if i['name'] != LAST_NAME:
                    print(i['name'])
                    RES.append(WeatherNow(city=i['name'],
                                          date_time=now.strftime(
                                              "%d/%m/%Y %H:%M:%S"),
                                          weather='{0:+3.0f}'.format(
                                              i['main']['temp']),
                                          description=i['weather'][0][
                                              'description']))
                    LAST_NAME = i['name']

        WeatherNow.objects.bulk_create(RES)
    except Exception as e:
        print("Exception (find):", e)
        pass
