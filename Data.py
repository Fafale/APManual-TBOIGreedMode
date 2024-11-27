import json
import logging
import os
import pkgutil

from .DataValidation import DataValidation, ValidationError

from .hooks.Data import \
    after_load_game_file, \
    after_load_item_file, after_load_location_file, \
    after_load_region_file, after_load_category_file, \
    after_load_meta_file

#All Characters List
characters_list = [
    "???",
    "Apollyon",
    "Azazel",
    "Bethany",
    "Cain",
    "Eden",
    "Eve",
    "Isaac",
    "Jacob & Esau",
    "Judas",
    "Keeper",
    "Lazarus",
    "Lilith",
    "Magdalene",
    "Samson",
    "Tainted ???",
    "Tainted Apollyon",
    "Tainted Azazel",
    "Tainted Bethany",
    "Tainted Cain",
    "Tainted Eden",
    "Tainted Eve",
    "Tainted Forgotten",
    "Tainted Isaac",
    "Tainted Jacob",
    "Tainted Judas",
    "Tainted Keeper",
    "Tainted Lazarus",
    "Tainted Lilith",
    "Tainted Lost",
    "Tainted Magdalene",
    "Tainted Samson",
    "The Forgotten",
    "The Lost"
]

#Locations for each character
generic_char_locations = [
    ["CHAR - Hold 9 Coins",                "(|Unlock CHAR|)"],
    ["CHAR - Hold 18 Coins",               "(|Unlock CHAR| and {ItemValue(CHAR items:1)})"],
    ["CHAR - Hold 27 Coins",               "(|Unlock CHAR| and |CHAR Progressive Floor: 1| and {ItemValue(CHAR items:2)})"],
    ["CHAR - Hold 36 Coins",               "(|Unlock CHAR| and |CHAR Progressive Floor: 2| and {ItemValue(CHAR items:3)})"],
    ["CHAR - Hold 45 Coins",               "(|Unlock CHAR| and |CHAR Progressive Floor: 3| and {ItemValue(CHAR items:4)})"],
    ["CHAR - Hold 54 Coins",               "(|Unlock CHAR| and |CHAR Progressive Floor: 4| and {ItemValue(CHAR items:5)})"],
    ["CHAR - Hold 63 Coins",               "(|Unlock CHAR| and |CHAR Progressive Floor: 5| and {ItemValue(CHAR items:6)})"],
    ["CHAR - Hold 72 Coins",               "(|Unlock CHAR| and |CHAR Progressive Floor: 5| and {ItemValue(CHAR items:7)})"],
    ["CHAR - F1 - Clear Waves",            "(|Unlock CHAR|)"],
    ["CHAR - F1 - Clear Bosses",           "(|Unlock CHAR|)"],
    ["CHAR - F1 - Clear Nightmare",        "(|Unlock CHAR| and {ItemValue(CHAR items:1)})"],
    ["CHAR - F2 - Clear Waves",            "(|Unlock CHAR| and |CHAR Progressive Floor: 1| and {ItemValue(CHAR items:1)})"],
    ["CHAR - F2 - Clear Bosses",           "(|Unlock CHAR| and |CHAR Progressive Floor: 1| and {ItemValue(CHAR items:2)})"],
    ["CHAR - F2 - Clear Nightmare",        "(|Unlock CHAR| and |CHAR Progressive Floor: 1| and {ItemValue(CHAR items:2)})"],
    ["CHAR - F3 - Clear Waves",            "(|Unlock CHAR| and |CHAR Progressive Floor: 2| and {ItemValue(CHAR items:2)})"],
    ["CHAR - F3 - Clear Bosses",           "(|Unlock CHAR| and |CHAR Progressive Floor: 2| and {ItemValue(CHAR items:3)})"],
    ["CHAR - F3 - Clear Nightmare",        "(|Unlock CHAR| and |CHAR Progressive Floor: 2| and {ItemValue(CHAR items:3)})"],
    ["CHAR - F4 - Clear Waves",            "(|Unlock CHAR| and |CHAR Progressive Floor: 3| and {ItemValue(CHAR items:3)})"],
    ["CHAR - F4 - Clear Bosses",           "(|Unlock CHAR| and |CHAR Progressive Floor: 3| and {ItemValue(CHAR items:4)})"],
    ["CHAR - F4 - Clear Nightmare",        "(|Unlock CHAR| and |CHAR Progressive Floor: 3| and {ItemValue(CHAR items:4)})"],
    ["CHAR - F5 - Clear Waves",            "(|Unlock CHAR| and |CHAR Progressive Floor: 4| and {ItemValue(CHAR items:4)})"],
    ["CHAR - F5 - Clear Bosses",           "(|Unlock CHAR| and |CHAR Progressive Floor: 4| and {ItemValue(CHAR items:5)})"],
    ["CHAR - F5 - Clear Nightmare",        "(|Unlock CHAR| and |CHAR Progressive Floor: 4| and {ItemValue(CHAR items:5)})"],
    ["CHAR - F6 - Clear Waves",            "(|Unlock CHAR| and |CHAR Progressive Floor: 5| and {ItemValue(CHAR items:5)})"],
    ["CHAR - F6 - Clear Bosses",           "(|Unlock CHAR| and |CHAR Progressive Floor: 5| and {ItemValue(CHAR items:6)})"],
    ["CHAR - F6 - Clear Nightmare",        "(|Unlock CHAR| and |CHAR Progressive Floor: 5| and {ItemValue(CHAR items:6)})"],
    ["CHAR - Defeat Miniboss",             "(|Unlock CHAR| and |CHAR Progressive Floor: 6| and {ItemValue(CHAR items:7)})"],
    ["CHAR - Defeat Ultra Greed",          "(|Unlock CHAR| and |CHAR Progressive Floor: 6| and {ItemValue(CHAR items:8)})"]
]

#Items for each character, their amount, their value in logic and whether they're a progression item
generic_char_items = [
    ["CHAR Progressive Floor",          6, 0, True],
    ["CHAR Progressive Shop",           6, 2, True],
    ["CHAR Progressive Silver Item",    5, 1, True],
    ["CHAR Progressive Golden Item",    5, 2, True],
    ["CHAR Extra Coin",                15, 0, False],
]

#Amount of each item to be removed if character isn't included
item_amount = {
    "Floor":generic_char_items[0][1],
    "Shop":generic_char_items[1][1],
    "Silver":generic_char_items[2][1],
    "Golden":generic_char_items[3][1],
    "Coin":generic_char_items[4][1]
}

# blatantly copied from the minecraft ap world because why not
def load_data_file(*args) -> dict:
    fname = os.path.join("data", *args)

    try:
        filedata = json.loads(pkgutil.get_data(__name__, fname).decode())
    except:
        filedata = []

    return filedata

def convert_to_list(data, property_name: str) -> list:
    if isinstance(data, dict):
        data = data.get(property_name, [])
    return data


class ManualFile:
    filename: str
    data_type: dict|list
    
    def __init__(self, filename, data_type):
        self.filename = filename
        self.data_type = data_type

    def load(self):
        contents = load_data_file(self.filename)
        
        if not contents and type(contents) != self.data_type:
            return self.data_type()
        
        return contents


game_table = ManualFile('game.json', dict).load() #dict
item_table = convert_to_list(ManualFile('items.json', list).load(), 'data') #list
location_table = convert_to_list(ManualFile('locations.json', list).load(), 'data') #list
region_table = ManualFile('regions.json', dict).load() #dict
category_table = ManualFile('categories.json', dict).load() #dict
meta_table = ManualFile('meta.json', dict).load() #dict

# Removal of schemas in root of tables
region_table.pop('$schema', '')
category_table.pop('$schema', '')

# hooks
game_table = after_load_game_file(game_table)
item_table = after_load_item_file(item_table)
location_table = after_load_location_file(location_table)
region_table = after_load_region_file(region_table)
category_table = after_load_category_file(category_table)
meta_table = after_load_meta_file(meta_table)

# seed all of the tables for validation
DataValidation.game_table = game_table
DataValidation.item_table = item_table
DataValidation.location_table = location_table
DataValidation.region_table = region_table

validation_errors = []

# check that json files are not just invalid json
try: DataValidation.checkForGameBeingInvalidJSON()
except ValidationError as e: validation_errors.append(e)

try: DataValidation.checkForItemsBeingInvalidJSON()
except ValidationError as e: validation_errors.append(e)

try: DataValidation.checkForLocationsBeingInvalidJSON()
except ValidationError as e: validation_errors.append(e)


############
# If there are any validation errors, display all of them at once
############

if len(validation_errors) > 0:
    logging.error("\nValidationError(s): \n\n%s\n\n" % ("\n".join([' - ' + str(validation_error) for validation_error in validation_errors])))
    print("\n\nYou can close this window.\n")
    keeping_terminal_open = input("If you are running from a terminal, press Ctrl-C followed by ENTER to break execution.")
