from common import *
from inventory import *
import json

# read data
with open('src/data/inventory.json', 'r') as myFile:
    data = myFile.read()

inventory = Inventory(json.loads(data))
key = 9

while key != 0:
    # print menu
    clearConsole()
    print('[AVAILABLE OPERATIONS]\n')
    print('[1] - ADD')
    print('[2] - REMOVE')
    print('[3] - PRINT')
    print('[4] - SEARCH')
    print('[5] - RESUME VALUES')
    print('[0] - EXIT')

    # read input
    key = int(input('\n'))

    # input 1 - add items
    if key == 1:
        inventory.add()

    # input 2 - remove items
    if key == 2:
        clearConsole()
        print("[REMOVE]")
        inventory.remove()

    # input 3 - print items
    if key == 3:
        clearConsole()
        print("[PRINT]")
        inventory.printList()
        input('\nPress any key to proceed...')

    # input 4 - search items
    if key == 4:
        clearConsole()
        print("[SEARCH]")
        inventory.find()

    # input 5 - resume items value
    if key == 5:
        clearConsole()
        print("[RESUME VALUES]")
        inventory.resumeValue()

# save data
with open('src/data/inventory.json', 'w', encoding='utf-8') as myFile:
    json.dump(inventory.toJson(), myFile, ensure_ascii=False, indent=4)
