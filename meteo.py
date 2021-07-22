import json
from itertools import islice


class meteoObject:
    def __init__(self, measure_id, capteur_id, temperature, humidity, date):
        self.measure_id = measure_id
        self.capteur_id = capteur_id
        self.temperature = temperature
        self.humidity = humidity
        self.date = date


def hexa_to_temperature(hexadecimal):
    if (hexadecimal == ''):
        return;
    return int(hexadecimal, 16) / 10


# format date "2018/12/13 02:29:17"
def hexa_to_date(hexadecimal):
    if (hexadecimal == ''):
        return;
    return "2018/12/13 02:29:17";


def get_full_tag(string):
    start_index_tag_information = 76
    tag_length = int(string[start_index_tag_information:start_index_tag_information + 4], 16)
    tag = string[start_index_tag_information:start_index_tag_information + tag_length]
    print(tag)
    return tag

def get_tag_information(tag):
    tag = "m"

#tag1 = meteoObject()

tag = "001900020B06182660000E1E0"
def split_tag(tag):
    chunks = (4,2,2,2,9,4,2)
    assert len(tag) >= sum(chunks)
    it = iter(tag)
    result = [(''.join(islice(it, i))) for i in chunks]
    print(result)

    return result



def create_meteo_object_from_data(data):
    # dumps : convert data to a string of json
    # get id in string type

    l = []
    for x in range(len(data)):
        # get hexa data
        tab = split_tag(get_full_tag(data[x][1]))
        data2 = json.dumps(data[x][1])
        l.append(meteoObject(data[x][0],
                             tab[4],  # temp capteur id
                             hexa_to_temperature(tab[5]),
                             data[x][2],
                             hexa_to_date(data2[105:107])))

    return l


def toString(p):
    return f'Mesure n° {p.measure_id} : Capteur {p.capteur_id} : {p.temperature} C° : le {p.date} \n'
