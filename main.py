import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from prettytable import PrettyTable

# Set up the base URL
url = "https://www.tintenalarm.de/"

# Getting response from the base URL
response = requests.get(url)

# Parsing the response to HTML using beautiful soup
soup = BeautifulSoup(response.text, "html.parser")

# Finding all the supplier list
ink_toner_supplier = soup.find("div", {"id": "droppable1"})

# Getting all the links of suppliers
suppliers = ink_toner_supplier.select('a[href]')

# Initializing blank arrays
supplier_data = []

# Initializing Table
supplier_table = PrettyTable(['SN', 'Brand', 'Title', 'URL'])

# Index counter
index = 1

# Parsing supplier data
for link in suppliers:
    if (str(link.get('title')) != "") & (str(link.get('title')) != "None"):
        data = str(link.text) + "~" + str(link.get('title')) + "~" + str(link.get('href'))
        supplier_table.add_row([str(index), str(link.text), str(link.get('title')), str(link.get('href'))])
        index = index + 1
        supplier_data.append(data)

print(supplier_table)

# Set up the supplier URL
split_data = supplier_data[0].split("~")
url_supplier = split_data[2]

# Getting response from the supplier URL
response_supplier = requests.get(url_supplier)

# Parsing the response to HTML using beautiful soup
soup_supplier = BeautifulSoup(response_supplier.text, "html.parser")

# Finding all the supplier division
supplier_id_div = soup.find("div", {"class": "m_filterbutton4"})

# Finding all the supplier id
supplier_id = supplier_id_div.select('option')

# Initializing blank arrays
supplier_brand_id = []

# Initializing Brand Table
supplier_brand_id_table = PrettyTable(['SN', 'Brand', 'Brand ID'])

# Index counter
index = 1

for sup_id in supplier_id:
    if str(sup_id.get('value')) != "":
        supplier_brand_id_table.add_row([str(index), str(sup_id.text), str(sup_id.get('value'))])
        index = index + 1
        data = str(sup_id.text) + "~" + str(sup_id.get('value'))
        supplier_brand_id.append(data)
        if index > 18:
            break

print(supplier_brand_id_table)

# Initializing blank arrays
model_category_id = []

# Initializing model Category Table
model_category_table = PrettyTable(['SN', 'Model Category', 'Category ID'])

# Brand model Category URL
url_model_category = "https://www.tintenalarm.de/ajax_search_mobile.php"

# Index counter
index = 1

# Brand ID & Request Number with GET request
for brd_id in supplier_brand_id:
    # Splitting brand info
    split_data = brd_id.split("~")
    brand_name = split_data[0]
    brand_id = split_data[1]
    request_id = "1"
    PARAMS = {'root': brand_id, 'number': request_id}
    model_category_response = requests.get(url=url_model_category, params=PARAMS)

    # Parsing the response to HTML using beautiful soup
    soup_model_category = BeautifulSoup(model_category_response.text, "html.parser")

    # Finding all the model category
    model_id_div = soup_model_category.find("div", {"class": "m_filterbutton4"})

    # Finding all the supplier id
    model_category = model_id_div.select('option')

    # model Index counter
    model_index = 1

    for model_cat in model_category:
        if str(model_cat.get('value')) != "":
            model_category_table.add_row([str(model_index), str(model_cat.text), str(model_cat.get('value'))])
            model_index = model_index + 1
            data = str(model_cat.get('value'))
            model_category_id.append(data)

    # Initializing Brand Identifier Table
    model_brand_identity_table = PrettyTable(['SN', 'Brand', 'Brand ID', 'Total Models'])
    model_brand_identity_table.add_row([str(index), brand_name, brand_id, str(len(model_category_id))])

    print(model_brand_identity_table)
    print(model_category_table)

    break