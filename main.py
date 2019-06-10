import requests
import urllib.request
import time
from bs4 import BeautifulSoup

# Set up the base URL
url = "https://www.tintenalarm.de/"

# Getting response from the base URL
response = requests.get(url)

# Parsing the response to HTML using beautiful soup
soup = BeautifulSoup(response.text, "html.parser")

# Finding all the supplier list
ink_toner_supplier = soup.find("div", {"id": "droppable1"})