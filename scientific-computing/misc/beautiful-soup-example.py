import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup

url = input('Enter -')
html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
