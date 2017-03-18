import requests
import time
import json
from bs4 import BeautifulSoup
import urllib.parse

s = urllib.parse.quote_plus('out of order')
s = urllib.parse.quote_plus('傳統')
resp = requests.get('https://tw.dictionary.yahoo.com/dictionary?p='+s)
print(resp.text)