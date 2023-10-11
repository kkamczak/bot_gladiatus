from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from functions import puts, log_in, get_cookies_values, save_cookies, get_character_view
from settings import URL, MIN_HP
import globals as GLOBALS
import expeditions as EXPEDITION
import dungeons as DUNGEON
import circus_provinciarum as CP
import threading
from gui import Gui

# GUI
def run_interface():
    gui = Gui()
    gui.run()


# Loggin to Gladiatus page
def run_program():
    def update_options(window):
        GLOBALS.LEVEL = str(window.find_element("id", "header_values_level").text)

    # Starting google chrome
    s = Service("C:\chromedriver.exe")
    window = webdriver.Chrome(service=s)
    window.maximize_window()
    window.get(URL)

    time.sleep(2)

    # Load cookies from file and refresh
    get_cookies_values(window)
    window.refresh()

    time.sleep(2)
    log_in(window)

    get_character_view(window)

    update_options(window)



    while GLOBALS.RUNNING:

        print('------------------------------------------------------------------------------------------')
        time.sleep(5)

        save_cookies(window)

        if not GLOBALS.PAUSED:

            #check_for_character_view(window)

            if GLOBALS.DO_EXPEDITIONS and not GLOBALS.CLOSING: EXPEDITION.loop(window, MIN_HP)
            if GLOBALS.DO_DUNGEONS and not GLOBALS.CLOSING: DUNGEON.loop(window)
            if GLOBALS.DO_CP and not GLOBALS.CLOSING: CP.loop(window)
        else:
            puts("Działanie bota zostało wstrzymane...")

        update_options(window)

        if GLOBALS.CLOSING: GLOBALS.RUNNING = False


def start_program():
    # Configure Threads
    t1 = threading.Thread(target = run_program)
    t2 = threading.Thread(target = run_interface)

    # Start bot
    t1.start()
    t2.start()

    t1.join()
    t2.join()





