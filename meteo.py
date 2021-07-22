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
    if hexadecimal == '':
        return;
    n_hexa = hexadecimal[1:4]
    if int(hexadecimal[0:1]) == 4:
        return int(n_hexa, 16) / 10 * -1

    return int(n_hexa, 16) / 10


def get_full_tag(string):
    start_index_tag_information = 76
    tag_length = int(string[start_index_tag_information:start_index_tag_information + 4], 16) *2
    tag = string[start_index_tag_information:start_index_tag_information + tag_length]
    print(tag)
    return tag


def split_tag(tag):
    chunks = (4,2,2,2,8,4,2,2,6,8,4,2,2)
    assert len(tag) >= sum(chunks)
    it = iter(tag)
    result = [(''.join(islice(it, i))) for i in chunks]
    print(result)

    return result


def create_meteo_object_from_data(data):
    # dumps : convert data to a string of json
    l = []
    for x in range(len(data)):
        # get hexa data
        tab = split_tag(get_full_tag(data[x][1]))
        data2 = json.dumps(data[x][1])
        l.append(meteoObject(data[x][0], #measure id
                             tab[4],  # temp capteur id
                             hexa_to_temperature(tab[5]),
                             tab[6], #humidity
                             data[x][2]))

        capteur_number = int(data[x][1][83:84],16)
        if capteur_number == 2:
            l.append(meteoObject(data[x][0], #measure id
                             tab[9],  #capteur id
                             hexa_to_temperature(tab[10]), #temp°
                             tab[11], #humidity
                             data[x][2]))
    return l


def toString(p):
    return f'[==== Mesure n° {p.measure_id} le {p.date} ====] ' \
           f' \n Capteur {p.capteur_id} : {p.temperature} C°  \n'
