# Created by IAmSalt Salty. Owned by AtherActive
import os

def startSetup():

    os.system('echo *** Starting installation ***')
    print('')

    os.system('echo ** Installing requests **')
    os.system('pip install requests')

    print('Installation complete.')

    print('''
    ***************Finished****************
    * Setup has finished with the install *
    * Hope you enjoy! - AtherActive       *
    *  (You can now close this terminal)  *
    ***************************************
    
    ''')

def app_start():
    option = input('''
    *****************Install******************
    * Welcome to the EVEAPIDEMO Installation!*
    *                                        *
    * The script will do some required setup *
    * now. (Installing dependencies.)        *
    *                                        *
    * Type "start" once you are ready!       *
    ******************************************
    ''')

    try:
        if option == 'start':
            startSetup()
        else:
            print('''
**********Error**********
* An error occured. Try *
* again please!  :(     *
*************************
            ''')

    except:
         print('''
**********Error**********
* An error occured. Try *
* again please!  :(     *
*************************
            ''')

app_start()