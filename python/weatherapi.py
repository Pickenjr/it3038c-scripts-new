import json
import requests

print('Please enter your zipcode')
zip = input()
r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=%s,us&appid=c5801d0f3850e78ecdb6674693cf04d8' % zip)
data = r.json()
print(data)
