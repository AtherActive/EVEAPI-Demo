# EVEPy - EVE Online Library for Python
# Copyright (C) 2020 - AtherActive
# View terms in LICENSE.txt file.

import json as js
import requests as rq
import structures as stru
import settings
import csv


### Market related stuff

# If this function fails the app should close anyway, as it cannot function without this. No try statement is added here.
def ImportMarketData():
    print('''
    ******************************************
    * Market Data is being imported. Hold on *
    ******************************************
    ''')

    d = 0
    with open('typeids.csv', encoding='cp850') as f:
        d = dict(filter(None, csv.reader(f)))
    if settings.developerMode == 1:
        print(d)

    return d



def UpdateMarketValues(data, name, id=-1):
    # create structure for storage purposes
    dataStruct = stru.MarketItem()

    try:
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
    except data:
        print("An error occured while updating market values. Please try again or report this issue on Github.")

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

    try:
        url = 'https://api.evemarketer.com/ec/marketstat/json?typeid={}'.format(PullItemID(name))
        data = rq.get(url)
        jsData = data.json()

        if settings.developerMode == 1:
            stru.PrintS("Received from {}: ".format(url), jsData)


        itemStruct = UpdateMarketValues(jsData, name, PullItemID(name))
    except:
        print('An error occured while pulling data from the API. This may be a connection issue.')
        itemStruct = stru.MarketItem()

    return itemStruct

# Finds Item ID needed for pulling market data.
def PullItemID(itemname):

    output = 0

    try:
        output = itemDB.get(itemname)
    except:
        print('Something went wrong.')

    return output


#### Incursion related stuff

def PullIncursionData(method=str('EVEPY')):
    #Pulls data from URL and converts it into JSON
    url = 'https://esi.evetech.net/latest/incursions/?datasource=tranquility'
    try:
        data = rq.get(url)
        jsData = data.json()
    except ConnectionError:
        print('A connection error occured. Are you online?')
    
    try:
        if method == 'EVEPY':
            #Init var to store incursions
            incursions = []

            #Set lenght for loop. yay
            length = len(jsData)

            # Every loop incursion data will be read by __parseIncursionData(). It then gets added to var Incursions.
            for i in range(length):
                # Add data to var Incursion.
                incursions.append(__parseIncursionData(jsData, i))
                # If Dev mode, print some debug. Can be toggled in settings.py
                if settings.developerMode == 1:
                    print(incursions[i].constellation_id)

            return incursions
        else:
            # Returns the RAW JSON data. Can be sued to make your own structues etc.
            return jsData
    except:
        print('Something went wrong while processing data. Please report this on our Github page.')

# Basically parses the input data in a decent manner. No comments needed really.
def __parseIncursionData(jsData, i):
    try:
        icstruct = stru.Incursion()

        icstruct.constellation_id = jsData[i]['constellation_id']
        icstruct.constellation_name = 'none'
        icstruct.staging = jsData[i]['staging_solar_system_id']
        icstruct.region_name = ResolveSystemNames(icstruct.constellation_id, 'con-reg')
        icstruct.status = jsData[i]['state']
        icstruct.systems_id = jsData[i]['infested_solar_systems']
        icstruct.systems_names = ResolveSystemNames(jsData[i]['infested_solar_systems'], 'system')
        icstruct.staging_name = ResolveSystemNames(jsData[i]['staging_solar_system_id'])
    except:
        print('An error occured while updating Incursion values. Please report this issue on our Github page.')
        icstruct = stru.Incursion()

    return icstruct
    
# Resolves names for systems, regions and constellations. Still WIP.
def ResolveSystemNames(id, mode='constellation'):
    #init value
    output_name = 'none'

    try:
        # If constellation, pull data and find region name.
        if mode == 'con-reg':
            url = 'https://www.fuzzwork.co.uk/api/mapdata.php?constellationid={}&format=json'.format(id)
            data = rq.get(url)
            jsData = data.json()
            output_name = jsData[0]['regionname']
    
    # Pulls system name form Fuzzwork.co.uk. 
        elif mode == 'system':
            #Convert output to a list.
            output_name = []
            lenght = len(id)
            # Pulls system name from Fuzzwork. Not that hard.
            for i in range(lenght):
                url = 'https://www.fuzzwork.co.uk/api/mapdata.php?solarsystemid={}&format=json'.format(id[i])
                data = rq.get(url)
                jsData = data.json()

                output_name.append(jsData[i]['solarsystemname'])
                
    except ConnectionError:
        print('A connection error occured. Are you online?')

    except:
        print('An error occured while updating system information. Please report this on Github fi it is not a connection issue.')
        
    return output_name

### Alliances List

# Pulls raw JSON data from API about alliances.
def PullAllianceIDList(datasource='tranquility'):
    try:
        url = 'https://esi.evetech.net/latest/alliances/?datasource={}'.format(datasource)
        data = rq.get(url)

        #Debug codes
        if settings.statusCodes == 1:
            print(data.status_code)
            
        return data.json()
    except ConnectionError:
        print('A connection error occured. Please check your connection.')
    except:
        print('An error occured. Please read the detailed message if needed.')

### NPC Corps

def PullNPCCorpsID(datasource='tranquility'):
    try:
        url = 'https://esi.evetech.net/latest/corporations/npccorps/?datasource={}'.format(datasource)
        data = rq.get(url)

        if settings.statusCodes == 1:
            print(data.status_code)
        
        return data.json()
    except:
        print('An error occured.')

### Factional Warfare

# Currently not active due to some issues.
def PullFWWars(method='EVEPy'):
    active = 0 # Currently disabled this function for future expansion purposes
    if active == 1:
        try:
            url = 'https://esi.evetech.net/latest/fw/wars/?datasource=tranquility'
            data = rq.get(url)
            jsdata = data.json()

            return jsdata
        except:
            print('An error occured while pulling FW Data.')
    else:
        print('Function is not supported at the moment.')

### Industry index list

def PullIndyIndexList(method='JSON'):
    url = 'https://esi.evetech.net/latest/industry/systems/?datasource=tranquility'
    data = rq.get(url)
    jsData = data.json()

    if method == 'JSON':
        return jsData

# Required init.
itemDB = ImportMarketData()
