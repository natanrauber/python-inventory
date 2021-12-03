from common import *
from item import *
import json


class Inventory:  # define class Inventory

    # constructor
    def __init__(self, *args):
        self.itemList = []

        if len(args) > 0:
            self.fromJson(args[0])

    # attributes
    itemList: list[Item]

    # Inventory from JSON
    def fromJson(self, jsonMap):
        self.itemList = []
        for element in jsonMap:
            item: Item = Item(element)
            print(item.name)
            self.itemList.append(item)

    # Inventory to JSON
    def toJson(self):
        itemList = []
        for item in self.itemList:
            itemList.append(item.toJson())
        return itemList

    # add inventory item
    def add(self):
        key = 'Y'
        while key == 'Y':
            clearConsole()
            print("[INPUT]")
            item = Item(
                serial=input('\nSerial: '),
                name=input('Name..: '),
                value=float(input('Value.: ')),
            )
            self.itemList.append(item)
            key = input('\nType \'Y\' to proceed input: ').upper()
        self.sortList()

    # remove inventory item
    def remove(self):

        # enter item serial
        param = input('\nEnter serial: ')

        # create new inventory to store items that correspond to search params
        foundItems = Inventory()

        # search and remove items
        for item in self.itemList:
            if item.serial == param:
                foundItems.itemList.append(item)
                self.itemList.remove(item)

        # print removed items
        if len(foundItems.itemList) > 0:
            print('Removed ', len(foundItems.itemList), ' item(s):')
            foundItems.printList()
        else:
            print('Removed 0 item(s)')
        input('\nPress any key to proceed...')

    # print inventory items
    def printList(self):
        if len(self.itemList) > 0:
            for item in self.itemList:
                print('\nSerial: ', item.serial)
                print('Name..: ', item.name)
                print('Value.: ', item.value)
        else:
            print('\nEmpty inventory')

    # find inventory item
    def find(self):

        # enter search key (serial or name)
        param = input('\nEnter search key: ')

        # create Inventory.itemList to store items that correspond to search params
        foundItems = Inventory()

        # search items
        for item in self.itemList:
            if item.serial == param or item.name == param:
                foundItems.itemList.append(item)

        # print items that correspond to search params
        if len(foundItems.itemList) > 0:
            print('Found ', len(foundItems.itemList), ' item(s):')
            foundItems.printList()
        else:
            print('Found 0 item(s)')
        input('\nPress any key to proceed...')

    # resume inventory items value
    def resumeValue(self):
        valueList = []
        for item in self.itemList:
            valueList.append(item.value)
        if len(valueList) > 0:
            print('\nHighest value: ', max(valueList))
            print('Lowest value.: ', min(valueList))
            print('Total........: ', sum(valueList))
        else:
            print('\nEmpty inventory')

        input('\nPress any key to proceed...')

    # sort inventory
    def sortList(self):
        self.itemList.sort(key=self.sortKey)

    # sort criteria
    def sortKey(self, item: Item):
        return int(item.serial)
