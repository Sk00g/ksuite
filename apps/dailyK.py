
# pull from pdata all settings (weather endpoint, GMail creds, Asana creds, bible API, news article)

# pull weather (today detailed + 3 day forecast)

# pull inbox statuses

# pull Asana tasks

# pull REMEMBERs / TODOs

# pull interesting article

# pull chapter

import sys
import json
import tools.kterm as term
from apps.app_base import AppBase
from datetime import datetime

APP_NAME = "Daily K"
APP_VERSION = "V1.01.190204"
APP_KEY = "daily"
APP_DESCRIPTION = "Interesting and helpful daily information, all in one place"



class DailyK(AppBase):
    def __init__(self, terminal):
        super().__init__(APP_NAME, APP_VERSION, APP_KEY, APP_DESCRIPTION, terminal)

        self.title = None
        self.options = None

    def display_weather(self):
        # try:
        #     with open('pdata/daily/api.json', 'r') as file:
        #         api_data = json.load(file)['weather']
        #     data = KClient.get_data(
        #         api_data['host'], api_data['url'], cityId=api_data['cityId'], key=api_data['key'])

        #     with open('pdata/daily/lastWeatherRead.json', 'w') as file:
        #         json.dump(data, file)
        # except Exception as err:
        #     self.term.print_line('Querying weather data failed: %s' % str(err))
        #     return

        # Uncomment this if you don't want to actually call API
        with open('pdata/daily/lastWeatherRead.json', 'r') as file:
            data = json.load(file)

        # make into collapsable section?
        term.Header(0, 5, 'Weather')

        sunrise = datetime.fromtimestamp(data['sys']['sunrise'])
        sunset = datetime.fromtimestamp(data['sys']['sunset'])
        tokens = str(sunset - sunrise).split(':')
        day_length = "%s hours %s minutes" % (tokens[0], tokens[1])

        bullets = [
            {'bold': True, 'value': data['weather'][0]['main']},
            {'key': "Temperature", 'bold': True,
                'value': "%s °C" % (data['main']['temp'] - 273.15)},
            {'key': "Humidity", 'value': "%s%%" % data['main']['humidity']},
            {'key': "Visibility", 'value': data['visibility']},
            {'key': "Wind", 'value': "%s km/h" % data['wind']['speed']},
            {'key': "Sunrise", 'value': sunrise.strftime("%H:%M")},
            {'key': "Sunset", 'value': sunset.strftime("%H:%M")},
            {'key': "Day Length", 'value': day_length}
        ]
        term.BulletList(0, 6, bullets)

    def rename_title(self, new_title):
        self.title.text = new_title

    def initialize(self):
        self.title = term.Title(0, 0, "Daily K")

        self.display_weather()

        options = [
            { "text": "First option", "action": lambda: self.rename_title("First") },
            { "text": "Second option", "action": lambda: self.rename_title("Second") },
            { "text": "Third option", "action": self.rename_title },
        ]

        self.options = term.Select(0, 15, options, symbol='*')

        self.term.show_cursor(False)

        return True

    def destruct(self):
        pass

    def update(self, input):
        self.options.receive_input(input)

        return False

    def prompt(self):
        self.term.print_line('')
        self.term.print_line('')
        pass

