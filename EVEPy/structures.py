# EVEPy - EVE Online Library for Python
# Copyright (C) 2020 - AtherActive
# View terms in LICENSE.txt file.

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

@dataclass
class FactionWars:
    attackerID = -1
    defenderID = -1


@dataclass
class Incursion:
    constellation_id = int
    constellation_name = str

    staging = int
    staging_name = str

    systems_id = list
    systems_names = list
    region_name = str
    status = str

    def ___init___(self):
        self.constellation_id = -1
        self.constellation_name = 'undefined'

        self.staging = -1
        self.staging_name = 'undefined'

        self.systems_id = []
        self.systems_names = []
        self.region_name = 'undefined'
        self.status = 'unknown'

def PrintS(message, content):
    if message == "":
        message = "Message: "
    else:
        print(message, content)
