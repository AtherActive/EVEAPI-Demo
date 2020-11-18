# EVEPy - EVE Online Library for Python
# Copyright (C) 2020 - AtherActive
# View terms in LICENSE.txt file.

# 
# This file is more or less a demo for me to test features properly, and is by no means an actual terminal app to use.
#


from os import system
import os
from time import sleep

# A var used to decide wether to add a path or not. Only needed if you cannot open any files here.
addpath = 1

def runFile(path):
    try:
        if addpath == 1:
            system('python {}{}{}'.format(os.getcwd(), '/EVEPy/', path))
        else:
            system('python \{}{}'.format(os.getcwd(), path))
    except:
        print('An error ocurred during runtime. Please report this on github, as this is not intended!')

def app_run():
    print('''
    Menu Demo text
    999: Exit
    001: MarketApp
    002: IncursionApp
    801: Toggle AddPath (default=on)
    ''')
    # Decide what you want to do
    option = input()

    if option == '999':
        exit()

    # 800+ is config numbers.
    elif option == '801':
        if addpath == 1:
            addpath = 0
        else:
            addpath = 1
        app_run()

    elif option == '001':
        runFile('marketapp.py')
        app_run()

    elif option == '002':
        runFile('incursionapp.py')
        app_run()
app_run()