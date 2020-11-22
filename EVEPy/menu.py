# EVEPy - EVE Online Library for Python
# Copyright (C) 2020 - AtherActive
# View terms in LICENSE.txt file.

# 
# This file is more or less a demo for me to test features properly, and is by no means an actual terminal app to use.
#


from os import system
from time import sleep
import os
import settings

def configMode():
    print('''
***********
Config Mode
***********
    801: Toggle Addpath (Required for running out of editor)
    802: Toggle Developer Mode (Shows some more debug data.)
    999: Quit to menu  
    ''')

    option = input()

    # Wether you want to use addpath feature. Needed if running inside editor
    if option == '801':
        if settings.addpath == 1:
            settings.addpath = 0
            print(settings.addpath)
            configMode()
        else:
            settings.addpath = 1
            print(settings.addpath)
            configMode()

    # Toggle developer mode
    elif option == '802':
        if settings.developerMode == 1:
            settings.developerMode = 0
            print(settings.developerMode)
            configMode()
        else:
            settings.developerMode = 1
            print(settings.developerMode)
            configMode()

    elif option == '999':
        app_run()

def runFile(path):
    try:
        if settings.addpath == 1:
            system('python {}{}{}'.format(os.getcwd(), '/EVEPy/', path))
        else:
            system('python {}/{}'.format(os.getcwd(), path))
    except:
        print('An error ocurred during runtime. Please report this on github, as this is not intended!')

def app_run():
    print('''
**************
Developer Menu
**************
    001: MarketApp
    002: IncursionApp
    800: Enter config mode
    999: Exit
    ''')
    # Decide what you want to do
    option = input()

    if option == '999':
        exit()

    # 800+ is config numbers.
    elif option == '800':
        configMode()

    # Market app
    elif option == '001':
        runFile('marketapp.py')
        app_run()
    
    # Incursion App
    elif option == '002':
        runFile('incursionapp.py')
        app_run()
    else:
        print('This command does not exist.')
        app_run()
        
app_run()