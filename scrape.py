import requests
from bs4 import BeautifulSoup

url= 'https://store.steampowered.com/explore/new/'

response= requests.get(url)
print(response.status_code)