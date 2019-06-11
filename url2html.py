import requests
from bs4 import BeautifulSoup


def get(url):
    # Getting response from the URL
    response = requests.get(url)

    # Parsing the response to HTML using beautiful soup
    soup = BeautifulSoup(response.text, "html.parser")

    return soup