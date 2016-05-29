from pprint import pprint
import json
import requests
r = requests.get('http://api.openweathermap.org/data/2.5/weather?id=4156404&APPID=ab6938454e4a68abb2920603ceac03a8')
pprint(r.json())
if(r.ok):
    weather = json.loads(r.content.decode('utf-8'))
    if(weather['main']['temp_max'] > 310):
        print(weather['main']['temp_max'])
    if(weather['main']['temp_min'] < 500):
        print(weather['main']['temp_min'])

