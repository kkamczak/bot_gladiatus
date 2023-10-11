from functions import puts, check_for_notifications, check_if_dungeon_on_cooldown
import selectors as SELECTORS
import time


def loop(window):

    time.sleep(1)
    # If cannot determine cooldown time, must be working or somethings wrong. Exit script
    if not check_if_dungeon_on_cooldown(window):
        puts("Exiting dungeons - there is cooldown")
        return
    puts("Doing dungeon")

    check_for_notifications(window)

    # Check if we need to exit before delay
    if SELECTORS.get_dungeons_points(window) <= 0:
        puts("Exiting dungeon script - too low points")
        return

    # Go to dungeons
    puts("Entering dungeons")

    dungeon_bar = SELECTORS.get_dungeon_bar(window)
    if (dungeon_bar):
        #window.execute_script("arguments[0].click();", dungeon_bar)
        dungeon_bar.click()
    else:
        puts('Cannot click on dungeon bar')
        return

    # Go to dungeon tab
    puts("Clicking on dungeon tab")

    time.sleep(1)

    tab = SELECTORS.get_dungeon_tab(window)
    if (tab):
        #window.execute_script("arguments[0].click();", tab)
        tab.click()
    else:
        puts('Cannot click on dungeon bar')
        return

    time.sleep(1)

    # Dificulty 1
    puts("Selecting first difficulty")

    dif1 = SELECTORS.get_dungeon_dif1(window)
    if (dif1):
        window.execute_script("arguments[0].click();", dif1)
        #dif1.click()
    else:
        puts("Couldn't select first difficulty, maybe already in a dungeon?")

    time.sleep(2)

    # Select first found label and click attack
    puts("Fighting in dungeon")
    areas = SELECTORS.get_dungeon_areas(window)

    if (areas):
        window.execute_script("arguments[0].click();", areas[0])
        #areas[0].click()
    else:
        puts('Cannot start fight with enemy.')
        return
