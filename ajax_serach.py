import requests
from bs4 import BeautifulSoup

url_search = "https://www.tintenalarm.de/ajax_search_mobile.php"


def series_parser(manufacturer_id):
    params = {'root': manufacturer_id, 'number': 2}
    response = requests.get(url=url_search, params=params)
    response_html = BeautifulSoup(response.text, "html.parser")
    return response_html


def model_parser(series_id):
    params = {'root': series_id, 'number': 2}
    response = requests.get(url=url_search, params=params)
    response_html = BeautifulSoup(response.text, "html.parser")
    return response_html