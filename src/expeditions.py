from selenium.common.exceptions import NoSuchElementException
import selectors as SELECTORS
from functions import check_if_expedition_on_cooldown, puts, check_for_notifications, check_hp
import time


def loop(window, max_hp):

    # If cannot determine cooldown time, must be working or somethings wrong. Exit script
    if not check_if_expedition_on_cooldown(window):
        puts("Exiting expeditions - there is cooldown.")
        return

    puts("Entering expeditions")

    check_for_notifications(window)

    # Check if we need to exit before delay
    if (SELECTORS.get_expeditions_points(window) <= 0):
        puts("Exiting expedition script - too low points.")
        return

    # Check if we need to eat
    if check_hp(window, max_hp):

        # Go to expeditions
        puts("Health good - going to expedition")
        try:
            window.find_element("css selector", "#cooldown_bar_expedition > a").click()  # Click on 'Na wyprawę'
        except NoSuchElementException:
            puts("Couldn't find expedition bar.")
            return


        # Attack first enemy
        time.sleep(2)
        try:
            first_enemy_button = window.find_element("css selector", '#expedition_list > div:nth-child(1) > div:nth-child(2) > button')
            first_enemy_button.click()
        except NoSuchElementException:
            puts("Couldn't find expedition enemy button.")
            return

        time.sleep(0.5)
        check_for_notifications(window)

        # Go back to character view
        time.sleep(2)

    else:  # Eat food
        puts('Exiting expedition - Too low health.')
        return
