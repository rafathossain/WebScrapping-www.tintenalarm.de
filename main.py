import manufacturer

# Manufacturer List Array View
# print(manufacturer.manufacturer_list)

# Manufacturer List Table View
# print(manufacturer.manufacturer_list_table)

#
# # Finding all the manufacturer id
# manufacturer_id_option =
#
# # Initializing blank arrays
# manufacturer_id = []
#
# # Initializing Manufacturer Table
# manufacturer_id_table = PrettyTable(['SN', 'Manufacturer', 'Manufacturer ID'])
#
# # Index counter
# index = 1
#
# for man_id in manufacturer_id_option:
#     if str(man_id.get('value')) != "":
#         manufacturer_id_table.add_row([str(index), str(man_id.text), str(man_id.get('value'))])
#         index = index + 1
#         data = str(man_id.text) + "~" + str(man_id.get('value'))
#         manufacturer_id.append(data)
#         if index > 18:
#             break
#
# print(manufacturer_id_table)
#
# # Initializing blank arrays
# series_id = []
#
# # Initializing Series Table
# series_table = PrettyTable(['SN', 'Manufacturer', 'Manufacturer ID', 'Series', 'Series ID'])
#
# # Manufacturer series URL
# url_series = "https://www.tintenalarm.de/ajax_search_mobile.php"
#
# # Index counter
# index = 1
#
# # Manufacturer ID & Request Number with GET request
# for brd_id in manufacturer_id:
#     # Splitting series info
#     split_data = brd_id.split("~")
#     manufacturer_name = split_data[0]
#     manufacturer_id_ex = split_data[1]
#     request_id = "1"
#     PARAMS = {'root': manufacturer_id_ex, 'number': request_id}
#     series_response = requests.get(url=url_series, params=PARAMS)
#
#     # Parsing the response to HTML using beautiful soup
#     soup_series = BeautifulSoup(series_response.text, "html.parser")
#
#     # Finding all the series
#     series_id_div = soup_series.find("div", {"class": "m_filterbutton4"})
#
#     # Finding all the series id
#     series = series_id_div.select('option')
#
#     # model Index counter
#     model_index = 1
#
#     for ser in series:
#         if str(ser.get('value')) != "":
#             series_table.add_row([str(model_index), manufacturer_name, manufacturer_id_ex, str(ser.text), str(ser.get('value'))])
#             model_index = model_index + 1
#             data = str(ser.text) + "~" + str(ser.get('value'))
#             series_id.append(data)
#
#     print(series_table)
#     break
#
# # Model ID Array
# model_id = []
#
# # Initializing Model Table
# model_table = PrettyTable(['SN', 'Series', 'Series ID', 'Model', 'Model ID'])
#
# # Model URL
# url_series = "https://www.tintenalarm.de/ajax_search_mobile.php"
#
# # Index counter
# index = 1
#
# # Series ID & Request Number with GET request
# for ser_id in series_id:
#     # Splitting series info
#     split_data = ser_id.split("~")
#     series_name = split_data[0]
#     series_id_ex = split_data[1]
#     request_id = "2"
#     PARAMS = {'root': series_id_ex, 'number': request_id}
#     model_response = requests.get(url=url_series, params=PARAMS)
#
#     # Parsing the response to HTML using beautiful soup
#     soup_model = BeautifulSoup(model_response.text, "html.parser")
#
#     # Finding all the series
#     model_id_div = soup_model.find("div", {"class": "m_filterbutton4"})
#
#     # Finding all the series id
#     model = model_id_div.select('option')
#
#     # model Index counter
#     model_index = 1
#
#     for mod in model:
#         if str(mod.get('value')) != "":
#             model_table.add_row([str(model_index), series_name, series_id_ex, str(mod.text), str(mod.get('value'))])
#             model_index = model_index + 1
#             model_id.append(str(mod.get('value')))
#     print(model_table)
#     break
#
# link = manufacturer_id[0].split("~")[1] + "_" + series_id[0].split("~")[1] + "_" + model_id[0]
# link = "https://www.tintenalarm.de/index.php?cPath=" + link
#
# # Getting response from the base URL
# response = requests.get(link)
#
# # Parsing the response to HTML using beautiful soup
# soup = BeautifulSoup(response.text, "html.parser")
#
# print(soup)