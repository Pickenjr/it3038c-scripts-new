import json
import requests

r = requests.get('http://localhost:3000')
data = r.json()
Widget1 = data[0]['name']
Color1 = data[0]['color']
Widget2 = data[1]['name']
Color2 = data[1]['color']
Widget3 = data[2]['name']
Color3 = data[2]['color']
WidgetX = data[3]['name']
Color4 = data[3]['color']

print(Widget1, "is", Color1)
print(Widget2, "is", Color2)
print(Widget3, "is", Color3)
print(WidgetX, "is", Color4)