import json


class Item:  # define class Item

    # constructor
    def __init__(self, *args, serial='', name='', value=''):
        self.serial = serial
        self.name = name
        self.value = value

        if len(args) > 0:
            self.fromJson(args[0])

    # attributes
    serial: str
    name: str
    value: float

    # Item from JSON
    def fromJson(self, jsonMap):
        self.serial = jsonMap['serial']
        self.name = jsonMap['name']
        self.value = jsonMap['value']

    # Item to JSON
    def toJson(self):
        return {
            'serial': self.serial,
            'name': self.name,
            'value': self.value,
        }
