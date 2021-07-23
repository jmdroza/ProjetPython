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
def hexa_to_humidity(hexa):
    if hexa == '' or hexa == 'FF':
        return;
    return int(hexa,16)

def get_full_tag(string):
    start_index_tag_information = 76
    tag_length = int(string[start_index_tag_information:start_index_tag_information + 5], 16) * 2
    tag = string[start_index_tag_information:start_index_tag_information + tag_length]
    print(tag)
    return tag


def split_tag(tag):
    tag_info_chunks = (4, 2, 2, 2)
    assert len(tag) >= sum(tag_info_chunks)
    it = iter(tag)
    info = [(''.join(islice(it, i))) for i in tag_info_chunks]

    tag_data_length = int(info[0], 16) * 2
    number_tag = int(info[2], 16)
    length_of_per_tag = int(info[3], 16) * 2
    print("tag_data_length = ", tag_data_length)
    print("number_tag = ", number_tag)
    print("tag_length = ", length_of_per_tag)
    print('\n')

    tagX = []
    for n in range(number_tag):
        print("boucle n°", n)
        temp = tag[10+length_of_per_tag*n:10+length_of_per_tag*(n+1)]
        tagX.append({"tagN":n, "capteur_id":temp[0:8], "status":temp[8:10], "battery_voltage":temp[10:14], "temperature":temp[14:18], "humidity":temp[18:20]})

    print(tagX)
    return tagX


def create_meteo_object_from_data(data):
    # dumps : convert data to a string of json
    l = []
    for x in range(len(data)):
        # get hexa data
        tab = split_tag(get_full_tag(data[x][1]))

        capteur_number = int(data[x][1][83:84], 16)
        for n in range(capteur_number):
            l.append(meteoObject(data[x][0],  # measure id
                                 tab[n]["capteur_id"],  # temp capteur id
                                 hexa_to_temperature(tab[n]["temperature"]),
                                 hexa_to_humidity(tab[n]["humidity"]),  # humidity
                                 data[x][2]))
    return l


def toString(p):
    return f'[==== Mesure n° {p.measure_id} le {p.date} ====] ' \
           f' \n Capteur {p.capteur_id} : {p.temperature} C° : {p.humidity}% humidité  \n'

