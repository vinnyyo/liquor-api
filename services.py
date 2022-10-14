import json
import copy

def get_status():
    shot_file = open('shot.json')
    data = json.load(shot_file)
    result = copy.deepcopy(data)
    result['take_shot'] = False
    result['ounces'] = 1.5
    with open('shot.json', 'w') as filewrite:
        json.dump(result, filewrite)
    return data

def take_shot():
    result = {}
    result['take_shot'] = True
    result['ounces'] = 1.5
    with open('shot.json', 'w') as filewrite:
        json.dump(result, filewrite)

def take_shot_o(ounces: float):
    result = {}
    result['take_shot'] = True
    result['ounces'] = ounces
    with open('shot.json', 'w') as filewrite:
        json.dump(result, filewrite)