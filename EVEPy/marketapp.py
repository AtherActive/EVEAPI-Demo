# EVEPy - EVE Online Library for Python
# Copyright (C) 2020 - AtherActive
# View terms in LICENSE.txt file.
import main as api
import terminal_messages as msg


def PrintData(id):
    data = api.PullDataFromAPI(id)
    url = 'https://evemarketer.com/types/{}'.format(data.itemID)


    print('''
****************-Market Info-****************
   Processed Item: {}
   Name:           {}              
                                   
   Buy Orders:                     
       Average:{:,}                  
       Volume: {:,}
       Max:    {:,}
       Min:    {:,}                  
                                   
   Sell Orders:                    
       Average:{:,}                  
       Volume: {:,}
       Max:    {:,}
       Min:    {:,}    
       
   URL: {}                                           
****************-Market Info-****************
'''
          .format(
        data.itemID,
        data.friendlyName,

        data.buyValues.avgPrice,
        data.buyValues.volume,
        data.buyValues.maxPrice,
        data.buyValues.minPrice,
        data.sellValues.avgPrice,
        data.sellValues.volume,
        data.sellValues.maxPrice,
        data.sellValues.minPrice,
        url
                  )
    )


def retry():
    choice = input(msg.retry)
    if choice == 'y':
        app_start()
    else:
        exit(0)

def app_pre():
    api.ImportMarketData()
    return

def app_start():
    print(msg.startup)

    name = input(msg.inputValue)

    print(msg.loading)
    try:
        PrintData(name)
    except:
        print('''
        *************************************************
        *An error occurred. Did you spell the name right?*
        *************************************************
        ''')
        app_start()

    retry()
    return 0


app_pre()
app_start()
