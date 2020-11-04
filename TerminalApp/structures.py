# Created by IAmSalt Salty

from dataclasses import dataclass

@dataclass
class ItemValues:
    avgPrice = -1
    volume = -1
    minPrice = -1
    maxPrice = -1

@dataclass
class MarketItem:
    itemID = -1
    friendlyName = "unknown"

    buyValues = ItemValues()
    sellValues = ItemValues()

def PrintS(message, content):
    if message == "":
        message = "Message: "
    else:
        print(message, content)

@dataclass
class Incursion:
    constellation_id = -1
    constellation_name = 'undefined'

    staging = -1
    staging_name = 'undefined'

    systems_id = []
    systems_names = []
    region_name = 'undefined'
    status = 'unknown'