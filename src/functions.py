from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
import time
from datetime import datetime
from settings import LOGIN, PASSWORD
import selectors as SELECTORS
import pickle
import globals as GLOBALS

def get_cookies_values(window):
    try:
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            try:
                window.add_cookie(cookie)
            except Exception as e:
                print(e)
    except Exception as e:
        print("Nie można załadować cookies")
        print(e)

def save_cookies(window):
    try:
        cookies = window.get_cookies()
        pickle.dump(cookies, open("cookies.pkl", "wb"))
    except Exception:
        puts("Nie udało się zapisać plików cookies")

def puts (text):
    date_time = datetime.now()
    message = '['+str(date_time.strftime("%Y/%m/%d, %H:%M:%S"))+'] '+ text
    file = open("automation.log","a")
    file.write(message+'\n')
    file.close()
    print(message)
    GLOBALS.INFORMATIONS.append(message)
    GLOBALS.INFORMATIONS.pop(0)

def check_if_expedition_on_cooldown(window):
    try:
        cooldown_bar_text = window.find_element("css selector", "#cooldown_bar_text_expedition").text
        if cooldown_bar_text == 'Na wyprawę':
            puts('Expedition ready')
            return True
        else:
            puts('Expedition not ready!')
            return False
    except NoSuchElementException:
        puts("Nie znaleziono przycisku 'Na wyprawę'")

def check_if_dungeon_on_cooldown(window):
    try:
        cooldown_bar_text = window.find_element("css selector", "#cooldown_bar_text_dungeon").text
        if cooldown_bar_text == 'Do lochów':
            puts('Dungeon ready')
            return True
        else:
            puts('Dungeon not ready!')
            return False
    except NoSuchElementException:
        puts("Nie znaleziono przycisku 'Do lochów'")

def check_if_circus_provinciarum_on_cooldown(window):
    try:
        cooldown_bar_text = window.find_element("css selector", "#cooldown_bar_text_ct").text
        if cooldown_bar_text == 'Do Circus Turma':
            puts('Circus Turma ready')
            return True
        else:
            puts('Circus Turma not ready!')
            return False
    except NoSuchElementException:
        puts("Nie znaleziono przycisku 'Do Circus Turma'")

def check_bonus(window):
    # Check for bonus link
    bonus_link = SELECTORS.get_bonus(window)

    if (bonus_link):
        bonus_link.click()
        puts("Clicking bonus link")
        return True

    puts("No bonus link")
    return False

def check_for_notifications(window):
    # Check for any notifications
    found = True
    if check_bonus(window):
        time.sleep(1)

    while found:
        link_notification = SELECTORS.get_notification(window)
        if not (link_notification):
            puts('No notifications found')
            time.sleep(2)
            return False

        try:
            link_notification.click()
            puts("Notification closed")
        except (NoSuchElementException, ElementNotVisibleException):
            found = False
            puts("No notifications found")
    time.sleep(2)
    return True

def check_for_ad(window):
    # Check for any notifications
    found = True
    if check_bonus(window):
        time.sleep(1)

    while found:
        ad = SELECTORS.get_ad(window)
        if not (ad):
            puts('Ad not found')
            time.sleep(2)
            return False
        try:
            ad.click()
            puts("Ad closed")
        except (NoSuchElementException, ElementNotVisibleException):
            found = False
            puts("No ad found")
    time.sleep(2)
    return True

def check_for_multiple_attack_warning(window):
    # Check for any notifications
    run = True

    while run:
        link_notification = SELECTORS.get_multiple_attack_warning(window)
        if not (link_notification):
            puts('No multiple attack warning found')
            time.sleep(2)
            return False

        try:
            window.execute_script("arguments[0].click();", link_notification)
            #link_notification.click()
            puts("Multiple attack warning closed")
            run = False
            time.sleep(2)
        except (NoSuchElementException, ElementNotVisibleException):
            run = False
            puts('No multiple attack warning found')
            return False
    time.sleep(2)
    return True

def check_hp(window, max_percentage):
    # Check if HP high enough
    puts("Checking if HP is at least ({0}%)".format(str(max_percentage)))

    hp_percentage = SELECTORS.get_current_hp_percentage(window)
    if (hp_percentage) and (hp_percentage >= max_percentage):
        return True

    return False

def check_for_character_view(window):
    is_on_view = False
    try:
        aktywne_okno = window.find_element("css selector", "#mainmenu > a.menuitem.active").get_attribute("title")
        if str(aktywne_okno) == 'Podgląd':
            is_on_view = True
    except NoSuchElementException:
        is_on_view = False
    if not is_on_view:
        puts('Changing to character view window.')
        time.sleep(1)
        character_view_button = window.find_element("xpath", "/html/body/div[1]/div/div[5]/div/div[1]/div[1]/div/a[1]")
        character_view_button.click()
        time.sleep(1)

def get_character_view(window):
    try:
        time.sleep(1)
        character_view_button = window.find_element("css selector", "#mainmenu > a:nth-child(1)")
        character_view_button.click()
        time.sleep(1)
    except Exception:
        print('Nie znaleziono przycisku Podgląd')

def log_in(window):
    # Find log in tab:
    try:
        login_button = window.find_element("xpath", "/html/body/div[1]/div/div/div/div[2]/div[2]/div[2]/div/ul/li[1]/span")
        login_button.click()
    except (NoSuchElementException, ElementNotVisibleException):
        puts("1. Logowanie nie udane - już zalogowano?")

    time.sleep(1)

    # Find login box and write login
    try:
        box_login = window.find_element("xpath", "/html/body/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/form/div[1]/div/input")
        box_login.click()
        box_login.send_keys(LOGIN)
    except (NoSuchElementException, ElementNotVisibleException):
        puts("2. Logowanie nie udane - już zalogowano?")
    time.sleep(1)

    # Find password box and write password
    try:
        box_password = window.find_element("xpath", "/html/body/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/form/div[2]/div/input")
        box_password.click()
        box_password.send_keys(PASSWORD)
    except (NoSuchElementException, ElementNotVisibleException):
        puts("3. Logowanie nie udane - już zalogowano?")
    time.sleep(2)

    # Click log in button
    try:
        login_button2 = window.find_element("xpath", "/html/body/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/form/p/button[1]/span")
        window.execute_script("arguments[0].click();", login_button2)
    except (NoSuchElementException, ElementNotVisibleException):
        puts("4. Logowanie nie udane - już zalogowano?")
    #login_button2.click()
    time.sleep(2)

    # Start server and change window focus
    window_before = window.window_handles[0]
    try:
        server_button = window.find_element("xpath", "/html/body/div[1]/div/div/div/div[2]/div[2]/div[2]/div/button/span[2]/span")
        window.execute_script("arguments[0].click();", server_button)
        #server_button.click()
    except (NoSuchElementException, ElementNotVisibleException):
        puts("5. Logowanie nie udane - już zalogowano?")
    time.sleep(2)

    window_after = window.window_handles[1]
    window.switch_to.window(window_after)

    time.sleep(2)


