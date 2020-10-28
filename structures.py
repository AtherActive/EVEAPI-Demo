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
    friendlyName = "none"

    buyValues = ItemValues
    sellValues = ItemValues