import json
import re


data = json.loads(input())
#data = [{"bus_id" : 128, "stop_id" : 1, "stop_name" : "Prospekt Avenue", "next_stop" : 3, "stop_type" : "S", "a_time" : "08:12"}, {"bus_id" : 128, "stop_id" : 3, "stop_name" : "Elm Street", "next_stop" : 5, "stop_type" : "O", "a_time" : "08:19"}, {"bus_id" : 128, "stop_id" : 5, "stop_name" : "Fifth Avenue", "next_stop" : 7, "stop_type" : "O", "a_time" : "08:25"}, {"bus_id" : 128, "stop_id" : 7, "stop_name" : "Sesame Street", "next_stop" : 0, "stop_type" : "F", "a_time" : "08:37"}, {"bus_id" : 256, "stop_id" : 2, "stop_name" : "Pilotow Street", "next_stop" : 3, "stop_type" : "S", "a_time" : "09:20"}, {"bus_id" : 256, "stop_id" : 3, "stop_name" : "Elm Street", "next_stop" : 6, "stop_type" : "", "a_time" : "09:45"}, {"bus_id" : 256, "stop_id" : 6, "stop_name" : "Abbey Road", "next_stop" : 7, "stop_type" : "O", "a_time" : "09:59"}, {"bus_id" : 256, "stop_id" : 7, "stop_name" : "Sesame Street", "next_stop" : 0, "stop_type" : "F", "a_time" : "10:12"}, {"bus_id" : 512, "stop_id" : 4, "stop_name" : "Bourbon Street", "next_stop" : 6, "stop_type" : "S", "a_time" : "08:13"}, {"bus_id" : 512, "stop_id" : 6, "stop_name" : "Abbey Road", "next_stop" : 0, "stop_type" : "F", "a_time" : "08:16"}]
['Fifth Avenue', 'Abbey Road']

fields = [
    {'name': 'bus_id', 'type': int, 'format': None, 'required': True},
    {'name': 'stop_id', 'type': int, 'format': None, 'required': True},
    {'name': 'stop_name', 'type': str, 'format': r'^[A-Z].* (Road|Avenue|Boulevard|Street)$', 'required': True},
    {'name': 'next_stop', 'type': int, 'format': None, 'required': True},
    {'name': 'stop_type', 'type': str, 'format': r'^(S|O|F)$', 'required': False},
    {'name': 'a_time', 'type': str, 'format': r'^[0-2]\d:[0-5]\d$', 'required': True},
]

demand = []
other = []

for item in data:
    if item['stop_type'] == 'O':
        demand.append(item['stop_name'])
    else:
        other.append(item['stop_name'])

print(demand)
print(other)

wrong = [x for x in demand if x in other]
wrong.sort()
print('On demand stops test:')
if wrong:
    print('Wrong stop type:', wrong)
else:
    print('OK')
