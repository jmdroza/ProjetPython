import json

class meteoObject:
    def __init__(self,id,capteur_id,temperature,humidity,date):
        self.id = id
        self.capteur_id = capteur_id
        self.temperature = temperature
        self.humidity = humidity
        self.date = date

def hexa_to_decimal(hexadecimal):
    if(hexadecimal == ''):
        return;
    return int(hexadecimal, 16)/10

def create_meteo_object_from_data(data):
    # dumps : convert data to a string of json
    # get id in string type
    l = []
    for x in range(len(data)):
        # get hexa data
        data2 = json.dumps(data[x][1])
        l.append(meteoObject(data[x][0],
                             data[x][2],
                             hexa_to_decimal(data2[101:105]),
                             hexa_to_decimal(data2[87:94]),
                             hexa_to_decimal(data2[105:107])))
    return l

def toString(p):
    return f'Capteur n° {p.id} : {p.temperature} C° \n'