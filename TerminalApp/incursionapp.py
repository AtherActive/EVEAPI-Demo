# EVEPy - EVE Online Library for Python
# Copyright (C) 2020 - AtherActive
# View terms in LICENSE.txt file.
import main as api
import terminal_messages as msg
from time import sleep


def PrintData():
    data = api.PullIncursionData('EVEPY')
    id = 0
    lenght = len(data)

    for i in range(lenght):
        print('Processing Data #{}'.format(i))
        print('''
************Incursion Status************
*   Constellation: {}
*   HQ System:     {}
*   Region:        {}
*
*   Systems:       {}
*    
*   Status:        {}
************Incursion Status************
    '''.format(
    data[i].constellation_name,
    data[i].staging_name,
    data[i].region_name,
    data[i].systems_names,
    data[i].status))
    id = id +1

def retry():
    choice = input(msg.retry)
    if choice == 'y':
        app_start()
    else:
        exit(0)

def app_pre():
    app_start()
    return

def app_start():
    PrintData()
    print('Refreshing in 60 seconds!')
    sleep(60)
    app_pre()
    return 0


app_pre()

