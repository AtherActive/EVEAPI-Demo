#Created by IAmSalt Salty

import settings
import main as api
import TerminalApp.terminal_messages as msg


def app_start():
    print(msg.startup)
    api.PullDataFromAPI(input(msg.inputValue))


app_start()