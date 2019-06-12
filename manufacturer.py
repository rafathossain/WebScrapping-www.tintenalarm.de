from prettytable import PrettyTable
import url2html

# Initializing Table
manufacturer_list_table = PrettyTable(['SN', 'Manufacturer', 'Manufacturer ID', 'Title', 'URL'])

# Initializing Manufacturer Array
manufacturer_list = []
manufacturer_list_temp = []
manufacturer_id_temp = []

# Manufacturer URL
manufacturer_url = "https://www.tintenalarm.de/"

# HTML data from the URL
manufacturer_html = url2html.get(manufacturer_url)

# Parse manufacturer information
manufacturer_div = manufacturer_html.find("div", {"id": "droppable1"})
manufacturer_anchor = manufacturer_div.select('a[href]')

# Index counter
index = 1

# Arrange manufacturer data
for data in manufacturer_anchor:
    if (str(data.get('title')) != "") & (str(data.get('title')) != "None"):
        array_data = str(index) + "~" + str(data.text) + "~" + str(data.get('title')) + "~" + str(data.get('href'))
        manufacturer_list.append(array_data)
        index = index + 1

# Get manufacturer ID
for data in manufacturer_list:
    split_data = data.split("~")
    manufacturer_url = split_data[3]

    # HTML data from the URL
    manufacturer_html = url2html.get(manufacturer_url)

    # Parse manufacturer information
    manufacturer_div = manufacturer_html.find("div", {"class": "m_filterbutton4"})
    manufacturer_id = manufacturer_div.select('option')

    # Index counter
    index = 1

    for m_id in manufacturer_id:
        if str(m_id.get('value')) != "":
            index = index + 1
            data = str(m_id.text) + "~" + str(m_id.get('value'))
            manufacturer_id_temp.append(data)

    break

# Index counter
index = 1

# Preparing manufacturer list
for data in manufacturer_list:
    split_data = data.split("~")
    manufacturer = split_data[1]
    manufacturer_title = split_data[2]
    manufacturer_url = split_data[3]
    for m_id in manufacturer_id_temp:
        split_data = m_id.split("~")
        if split_data[0] == manufacturer:
            array_data = str(index) + "~" + \
                         manufacturer + "~" + \
                         str(split_data[1]) + "~" + \
                         manufacturer_title + "~" + \
                         manufacturer_url
            manufacturer_list_temp.append(array_data)
            manufacturer_list_table.add_row([str(index), manufacturer, str(split_data[1]), manufacturer_title, manufacturer_url])
            index = index + 1
            break

manufacturer_list = manufacturer_list_temp