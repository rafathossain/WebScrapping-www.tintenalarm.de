import requests
import url2html


def get_product_hook(product_url):
    # HTML data from the URL
    product_list_html = url2html.get(product_url)

    # Parse manufacturer information
    products_div = product_list_html.findAll("div", {"class": "product-listing-text"})

    if len(products_div) != 0:
        for data in products_div:
            products = data.select('a')[0]
            array_data = products.text + "~" + products.get('href')
            return array_data
    else:
        return "Invalid URL"

# get_product_hook("https://www.tintenalarm.de/patronen-c-42184-69349-69438.html")