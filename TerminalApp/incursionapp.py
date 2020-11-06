#Created by IAmSalt Salty
import main as api
import terminal_messages as msg
from time import sleep


def PrintData(data):
    data = api.PullIncursionData()
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
    data[id].constellation_name,
    data[id].staging_name,
    data[id].region_name,
    data[id].systems_names,
    data[id].status))
    id = id +1
# ^^^ As of right now this system is being replaced and is NOT working.

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
    PrintData('no')
    return 0


app_pre()

