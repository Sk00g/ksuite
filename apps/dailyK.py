
# pull from pdata all settings (weather endpoint, GMail creds, Asana creds, bible API, news article)

# pull weather (today detailed + 3 day forecast)

# pull inbox statuses

# pull Asana tasks

# pull REMEMBERs / TODOs

# pull interesting article

# pull chapter

import pdata
import os
import sys, tty
import json
import time
from datetime import datetime
from tools.kclient import KClient
from tools.kterm import KTerm, TColor


APP_NAME = "Daily K"
APP_VERSION = "V1.01.190204"
APP_KEY = "daily"


class DailyK:
    def __init__(self, term):
        self.term = term

    def print_weather(self):
        # try:
        #     with open('pdata/daily/api.json', 'r') as file:
        #         api_data = json.load(file)['weather']
        #     data = KClient.get_data(api_data['host'], api_data['url'], cityId=api_data['cityId'], key=api_data['key'])
        #
        #     with open('pdata/daily/lastWeatherRead.json', 'w') as file:
        #         json.dump(data, file)
        # except Exception as err:
        #     self.term.print_line('Querying weather data failed: %s' % str(err))
        #     return

        # Uncomment this if you don't want to actually call API
        with open('pdata/daily/lastWeatherRead.json', 'r') as file:
            data = json.load(file)

        # make into collapsable section?
        self.term.print_header('Weather')

        sunrise = datetime.fromtimestamp(data['sys']['sunrise'])
        sunset = datetime.fromtimestamp(data['sys']['sunset'])
        tokens = str(sunset - sunrise).split(':')
        day_length = "%s hours %s minutes" % (tokens[0], tokens[1])

        bullets = [
            { 'bold': True, 'value': data['weather'][0]['main'] },
            { 'key': "Temperature", 'bold': True, 'value': "%s °C" % (data['main']['temp'] - 273.15) },
            { 'key': "Humidity", 'value': "%s%%" % data['main']['humidity'] },
            { 'key': "Visibility", 'value': data['visibility'] },
            { 'key': "Wind", 'value': "%s km/h" % data['wind']['speed'] },
            { 'key': "Sunrise", 'value': sunrise.strftime("%H:%M") },
            { 'key': "Sunset", 'value': sunset.strftime("%H:%M") },
            { 'key': "Day Length", 'value': day_length }
        ]
        self.term.print_bullets(bullets)

    def run(self):
        self.term.print_title('Daily K')

        self.print_weather()

        self.term.print('\n\n')


        while True:
            char = ord(sys.stdin.read(1))

            if char == 3:
                break



































