import time
from functions import puts
from selenium.common.exceptions import NoSuchElementException

# ---------------------------------------------------------------------------------------------------------------------
# EXPEDITIONS:

def get_expeditions_points(window):
    try:
        return int(window.find_element("css selector", "#expeditionpoints_value_point").text)
    except Exception:
        return False

# ---------------------------------------------------------------------------------------------------------------------
# DUNGEONS:

def get_dungeons_points(window):
    try:
        return int(window.find_element("css selector", "#dungeonpoints_value_point").text)
    except NoSuchElementException:
        return False

def get_dungeon_bar(window):
    time.sleep(1)
    try:
        return window.find_element("id", "cooldown_bar_dungeon")
    except NoSuchElementException:
        return False

def get_dungeon_tab(window):
    try:
        time.sleep(1)
        return window.find_element("css selector", "#mainnav > li > table > tbody > tr > td:nth-child(2) > a")
    except NoSuchElementException:
        puts("Cannot select dungeon tab.")
    return False


def get_dungeon_dif1(window):
    time.sleep(1)
    try:
        return window.find_element("css selector", "#content > div:nth-child(3) > div > form > table > tbody > tr > td:nth-child(1) > input")
    except NoSuchElementException:
        puts("Cannot select difficulty dungeon button.")
        return False

def get_dungeon_areas(window):
    try:
        return window.find_elements("css selector", "img[src = '//gf3.geo.gfsrv.net/cdne6/643cfe405fb9a1fbd99513f08ca7fe.gif']")
    except NoSuchElementException:
        return False

# ---------------------------------------------------------------------------------------------------------------------
# CIRCUS TURMA / PROVINCIARUM:

def get_circus_turma_bar(window):
    time.sleep(1)
    try:
        return window.find_element("id", "cooldown_bar_ct")
    except NoSuchElementException:
        return False

def get_cp_tab(window):
  try:
      time.sleep(1)
      return window.find_element("css selector", "#mainnav > li > table > tbody > tr > td:nth-child(4) > a")
  except NoSuchElementException:
      puts("Cannot select Circus Provinciarum tab.")
  return False



# ---------------------------------------------------------------------------------------------------------------------
# NOTIFICATIONS:

def get_bonus(window):
    try:
        return window.find_element("id", "linkLoginBonus")
    except NoSuchElementException:
        return False

def get_notification(window):
    found_text = 1
    try:
        notification = window.find_element("id", "blackoutDialognotification")
        found_text = str(notification.get_attribute("style")).find('display: block')
    except Exception:
        return False
    if found_text == 0:
        try:
            puts('Notification found')
            return window.find_element("id", "linknotification")
        except Exception:
            return False
    else:
        return False

def get_ad(window):
    try:
        add_x_button = window.find_element("css selector", "#MAX_9ca736a9 > div.openX_int_closeButton > a")
        return add_x_button
    except NoSuchElementException:
        return False


def get_multiple_attack_warning(window):
    found_text = 1
    try:
        notification = window.find_element("id", "blackoutDialogbod")
        found_text = str(notification.get_attribute("style")).find('display: block')
    except Exception:
        return False
    if found_text != -1:
        try:
            puts('Multiple attack warning found')
            time.sleep(1)
            #return window.find_element("css selector", "/html/body/div[6]/div[2]/table/tbody/tr/td[2]/div/input")
            return window.find_element("css selector", "#blackoutDialogbod > div.blackoutDialog_body.pngfix > table > tbody > tr > td:nth-child(2) > div > input")

        except NoSuchElementException:
            return False
    else:
        return False

# ---------------------------------------------------------------------------------------------------------------------
# HEALTH:

def get_current_hp_percentage(window):
    time.sleep(1)
    try:
        return int(window.find_element("id", "header_values_hp_percent").text[:-1])
    except NoSuchElementException:
        return False
