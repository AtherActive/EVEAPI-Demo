# Created by IAmSalt Salty with help of the EVEMarketer-API.

import json as js
import requests as rq
import structures as str
import settings
import csv


# Market related stuff
def ImportMarketData():
    print('''
    ******************************************
    * Market Data is being imported. Hold on *
    ******************************************
    ''')

    d = 0
    with open('/home/saltylelele/EVEAPI-Demo/TerminalApp/typeids.csv', encoding='cp850') as f:
        d = dict(filter(None, csv.reader(f)))
    if settings.developerMode == 1:
        print(d)

    return d


def UpdateMarketValues(data, name, id=-1):
    # create structure for storage purposes
    dataStruct = str.MarketItem

    # sets all values.....
    dataStruct.itemID = id
    dataStruct.friendlyName = name

    dataStruct.buyValues.avgPrice = data[0]['buy']['avg']
    dataStruct.buyValues.volume = data[0]['buy']['volume']
    dataStruct.buyValues.maxPrice = data[0]['buy']['max']
    dataStruct.buyValues.minPrice = data[0]['buy']['min']

    dataStruct.sellValues.avgPrice = data[0]['sell']['avg']
    dataStruct.sellValues.volume = data[0]['sell']['volume']
    dataStruct.sellValues.maxPrice = data[0]['sell']['max']
    dataStruct.sellValues.minPrice = data[0]['sell']['min']

    # debug :D
    if settings.developerMode == 1:
        print(data[0]['buy']['avg'])
        print(data[0]['buy']['volume'])
        print(data[0]['buy']['max'])
        print(data[0]['buy']['min'])
        print(data[0]['sell']['avg'])
        print(data[0]['sell']['volume'])
        print(data[0]['sell']['max'])
        print(data[0]['sell']['min'])

    return dataStruct

# does what it says. Takes the data form the API.
def PullDataFromAPI(name):

    url = 'https://api.evemarketer.com/ec/marketstat/json?typeid={}'.format(PullItemID(name))
    data = rq.get(url)
    jsData = data.json()

    if settings.developerMode == 1:
        str.PrintS("Received from {}: ".format(url), jsData)


    itemStruct = UpdateMarketValues(jsData, name, PullItemID(name))

    return itemStruct

def PullItemID(itemname):

    output = 0

    try:
        output = itemDB.get(itemname)
    except:
        print('Something went wrong.')

    return output

itemDB = ImportMarketData()


#Incursion related stuff

def PullIncursionData():
    #Pulls data from URL
    url = 'https://esi.evetech.net/latest/incursions/?datasource=tranquility'
    data = rq.get(url)

    jsData = data.json()
    length = len(jsData)
    print(length)


    incursions = []
    for i in range(length):
        icstruct = str.Incursion

        icstruct.constellation_id = jsData[i]['constellation_id']
        icstruct.constellation_name = 'none'
        icstruct.staging = jsData[i]['staging_solar_system_id']
        icstruct.region_name = ResolveSystemNames(icstruct.constellation_id, 'con-reg')
        icstruct.status = jsData[i]['state']
        icstruct.systems_id = jsData[i]['infested_solar_systems']
        icstruct.systems_names = ResolveSystemNames(jsData[i]['infested_solar_systems'], 'system')
        incursions.append(icstruct)
        print(incursions[i].region_name)

    return incursions

def ResolveSystemNames(id, mode='constellation'):
    temp = id
    output_name = 'none'

    
    if mode == 'con-reg':
        url = 'https://www.fuzzwork.co.uk/api/mapdata.php?constellationid={}&format=json'.format(id)
        data = rq.get(url)
        jsData = data.json()
        output_name = jsData[0]['regionname']

    elif mode == 'system':
 
        output_name = []
        lenght = len(id)

        for i in range(lenght):
            url = 'https://www.fuzzwork.co.uk/api/mapdata.php?solarsystemid={}&format=json'.format(id[i])
            data = rq.get(url)
            jsData = data.json()

            output_name.append(jsData[i]['solarsystemname'])
    
    return output_name
