import requests
from prettytable import PrettyTable
import series
import ajax_serach
import product_url
import csv
import url2html

# Initializing model array
product_list = []

# Initializing Table
product_list_table = PrettyTable(['SN', 'Manufacturer', 'Manufacturer ID', 'Series Name', 'Series ID', 'Model Name', 'Model ID', 'Product URL'])

# Index counter
index = 1

with open('tintealarm_product_url.csv', mode='w', newline='') as csv_file:

    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(
        ["Manufacturer Name", "Manufacturer ID", "Series Name", "Series ID", "Model Name", "Model ID", "Product List URL", "Product Title", "Product URL"])

    for series_data in series.series_list:
        serial_no = series_data.split("~")[0]
        manufacturer_name = series_data.split("~")[1]
        manufacturer_id = series_data.split("~")[2]
        series_name = series_data.split("~")[3]
        series_id = series_data.split("~")[4]
        model_html = ajax_serach.model_parser(series_id)
        if model_html.text.split("_")[0] == "products":
            model_name = "N/A"
            model_id = "N/A"
            product_url_postfix = manufacturer_id + "_" + series_id
            product_list_url = "https://www.tintenalarm.de/index.php?cPath=" + product_url_postfix
            product_list_url = requests.get(product_list_url).url
            # print(product_list_url)
            # HTML data from the URL
            product_list_html = url2html.get(product_list_url)
            # Parse manufacturer information
            products_div = product_list_html.findAll("div", {"class": "product-listing-text"})
            array_data = ""
            if len(products_div) != 0:
                for data in products_div:
                    products = data.select('a')[0]
                    product_title = products.text
                    product_urls = products.get('href')
                    array_data = str(
                        serial_no) + "~" + manufacturer_name + "~" + manufacturer_id + "~" + series_name + "~" + series_id + "~" + model_name + "~" + model_id + "~" + product_list_url + "~" + product_title + "~" + product_urls
                    product_list.append(array_data)
                    csv_writer.writerow(
                        [manufacturer_name, manufacturer_id, series_name, series_id, model_name, model_id,
                         product_list_url, product_title, product_urls])
                    index = index + 1
                    print(array_data)
            # else:
            #     array_data = str(
            #         serial_no) + "~" + manufacturer_name + "~" + manufacturer_id + "~" + series_name + "~" + series_id + "~" + model_name + "~" + model_id + "~" + product_list_url + "~" + "N/A" + "~" + "N/A"
            #     product_list.append(array_data)
            #     csv_writer.writerow(
            #         [manufacturer_name, manufacturer_id, series_name, series_id, model_name, model_id, product_list_url,
            #          product_title, product_urls])
            #     index = index + 1
            #     print(array_data)
        else:
            model_options = model_html.select('option')
            for opt in model_options:
                if str(opt.get('value')) != "":
                    model_name = opt.text
                    model_id = opt.get('value')
                    product_url_postfix = manufacturer_id + "_" + series_id + "_" + model_id
                    product_list_url = "https://www.tintenalarm.de/index.php?cPath=" + product_url_postfix
                    product_list_url = requests.get(product_list_url).url
                    # print(product_list_url)
                    # HTML data from the URL
                    product_list_html = url2html.get(product_list_url)
                    # Parse manufacturer information
                    products_div = product_list_html.findAll("div", {"class": "product-listing-text"})
                    array_data = ""
                    if len(products_div) != 0:
                        for data in products_div:
                            products = data.select('a')[0]
                            product_title = products.text
                            product_urls = products.get('href')
                            array_data = str(
                                serial_no) + "~" + manufacturer_name + "~" + manufacturer_id + "~" + series_name + "~" + series_id + "~" + model_name + "~" + model_id + "~" + product_list_url + "~" + product_title + "~" + product_urls
                            product_list.append(array_data)
                            csv_writer.writerow(
                                [manufacturer_name, manufacturer_id, series_name, series_id, model_name, model_id,
                                 product_list_url, product_title, product_urls])
                            index = index + 1
                            print(array_data)
                    # else:
                    #     array_data = str(
                    #         serial_no) + "~" + manufacturer_name + "~" + manufacturer_id + "~" + series_name + "~" + series_id + "~" + model_name + "~" + model_id + "~" + product_list_url + "~" + "N/A" + "~" + "N/A"
                    #     product_list.append(array_data)
                    #     csv_writer.writerow(
                    #         [manufacturer_name, manufacturer_id, series_name, series_id, model_name, model_id,
                    #          product_list_url,
                    #          product_title, product_urls])
                    #     index = index + 1
                    #     print(array_data)