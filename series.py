from prettytable import PrettyTable
import manufacturer
import ajax_serach
from prettytable import PrettyTable
import csv

# Initializing series array
series_list = []

# Initializing series table
series_table = PrettyTable(['SN', 'Manufacturer', 'Manufacturer ID', 'Series', 'Series ID'])

# Index counter
index = 1

with open('series_data.csv', mode='w', newline='') as csv_file:

    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    # Get manufacturer URL from the list
    for data in manufacturer.manufacturer_list:
        manufacturer_name = data.split("~")[1]
        manufacturer_id = data.split("~")[2]
        series_list_temp = ajax_serach.series_parser(manufacturer_id)
        series_options = series_list_temp.select('option')

        # Nested index
        index_sm = 1

        for series in series_options:
            if str(series.get('value')) != "":
                if index_sm == 1:
                    series_table.add_row(
                        [str(index), manufacturer_name, manufacturer_id, str(series.text), str(series.get('value'))])
                else:
                    series_table.add_row(
                        ["", "", "", str(series.text), str(series.get('value'))])

                array_data = str(index) + "~" + manufacturer_name + "~" + manufacturer_id + "~" + str(
                    series.text) + "~" + str(series.get('value'))
                series_list.append(array_data)
                csv_writer.writerow([str(index), manufacturer_name, manufacturer_id, str(series.text), str(series.get('value'))])

                index_sm = index_sm + 1
        index = index + 1