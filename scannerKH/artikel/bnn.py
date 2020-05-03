import csv
from datetime import datetime
#from models import Artikel


def import_data(source):
    pass

def update_data(source):
    pass

def _load_data_from_bnn(path):
    with open(path, newline='') as bnn_file:
        data = csv.reader(bnn_file, delimiter=';')
        header_data = data.__next__()
        artikel = []
        for row in data:
            artikel.append(row)

        footer_data = artikel[-1]
        artikel = artikel[-1]  # Remove footer

    header = _convert_header(header_data)
    footer = _convert_footer(footer_data)
    print(header)
    print(artikel[:10])
    print(artikel[-1:])
    print(footer)

def _strip_list(data):
    stripped_list = []
    for data_point in data:
        stripped_list.append(data_point.strip())
    return stripped_list

def _convert_date(date_string, format='%Y%m%d'):
    return datetime.strptime(date_string, format)

def _convert_header(header_data):
    stripped_data = _strip_list(header_data)
    return {
        'kennung': stripped_data[0],
        'version': int(stripped_data[1]),
        'zeichensatz': int(stripped_data[2]),
        'versenderadresse': stripped_data[3],
        'umfang': stripped_data[4],
        'inhalt': stripped_data[5],
        'preiswaehrung': stripped_data[6],
        'datum_ab': _convert_date(stripped_data[7]),
        'datum_bis': _convert_date(stripped_data[8]),
        'abgabedatum': _convert_date(stripped_data[9] + stripped_data[10], '%Y%m%d%H%M'),
        'dateizaehler': int(stripped_data[11]),
    }

def _convert_footer(footer_data):
    stripped_data = _strip_list(footer_data)
    return {
        'kennung1': stripped_data[0],
        'kennung2': stripped_data[1],
        'dateizaehler': int(stripped_data[2]),
    }