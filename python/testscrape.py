import requests, re
from bs4 import BeautifulSoup

r = requests.get("https://www.youtube.com/watch?v=-ndwmvIwQmo").content
soup = BeautifulSoup(r, 'lxml')
div_a = soup.findAll('div')
span = div_a[1].find('span',class_='watch-title').text.strip()
title = span
span = div_a[1].find(class_='watch-view-count').text.strip()
count = span
print("The videos title is %s and has %s." %(title, count))
