from functions import puts, check_for_notifications, check_if_circus_provinciarum_on_cooldown, check_for_multiple_attack_warning
import selectors as SELECTORS
import time
from settings import enemies_cp, BLACK_LIST

# People that you losing with


def loop(window):

    time.sleep(1)
    # If cannot determine cooldown time, must be working or somethings wrong. Exit script
    if not check_if_circus_provinciarum_on_cooldown(window):
        puts("Exiting Circus Provinciarum - there is cooldown")
        return

    puts("Doing Circus Provinciarum")

    check_for_notifications(window)

    ct_bar = SELECTORS.get_circus_turma_bar(window)
    if (ct_bar):
        ct_bar.click()
    else:
        puts('Cannot click on Circus Turma bar')
        return

    # Go to Circus Provinciarum tab
    puts("Clicking on Circus Provinciarum tab")

    check_for_notifications(window)

    tab = SELECTORS.get_cp_tab(window)
    if (tab):
        tab.click()
    else:
        puts('Cannot click on Circus Provinciarum bar')
        return

    time.sleep(1)
    # Checking for Enemy:
    puts("Aktualna czarna lista: " + str(BLACK_LIST))
    my_level = str(window.find_element("id", "header_values_level").text)
    fight_id = -1
    enemy_name = ''
    enemy_lvl = ''
    #BLACK_LIST = ['Lisica', '[AZOV]Otaman*', 'Cytruss', 'Grzyb', 'Spycimir', 'Quorod', 'Jimmy', 'Maciej']
    for i, enemy in enumerate(enemies_cp):
        on_black_list = False
        enemy_name = str(window.find_element("css selector", enemy[0]).text)
        enemy_lvl = str(window.find_element("css selector", enemy[1]).text)
        puts("Sprawdzam " + enemy_name + " czy nadaje się do walki.")
        if bool(BLACK_LIST):
            for opponent in BLACK_LIST:
                if str(opponent) == enemy_name:
                    on_black_list = True
                    #time.sleep(1)
                    break
        if on_black_list:
            puts(" Ten przeciwnik jest na czarnej liście, szukam dalej.")
            #time.sleep(1)
            continue
        if abs(int(enemy_lvl) - int(my_level)) > 5:
            puts(enemy_name + " has too high level, looking for another opponent.")
            continue

        puts(enemy_name + " - ten przeciwnik jest odpowiedni")
        fight_id = i
        break

    check_for_notifications(window)

    if fight_id != -1:
        puts("Attacking enemy " + enemy_name)

        enemy_attack = window.find_element("css selector", enemies_cp[fight_id][2])
        enemy_attack.click()
        time.sleep(1)

        if not check_for_multiple_attack_warning(window):
            puts(str(window.find_element("css selector", "#reportHeader > table > tbody > tr > td:nth-child(2)").text))
            winner = str(window.find_element("css selector", "#reportHeader > table > tbody > tr > td:nth-child(2)").text).find('Krankenkapepe')
            if int(winner) == -1:
                BLACK_LIST.append(enemy_name)
                puts("Dodano " + enemy_name + " do czarnej listy z powodu przegranej")
        else:
            BLACK_LIST.append(enemy_name)
            puts("Dodano " + enemy_name + " do czarnej listy z powodu zbyt dużej ilości ataków w tym dniu.")
    else:
        puts("Nie znaleziono przeciwnika, wybrano wyszukanie nowych oponentów")
        time.sleep(1)
        search_for_other_opponents = window.find_element("css selector", "#content > article > form > input")
        #search_for_other_opponents.click()
        window.execute_script("arguments[0].click();", search_for_other_opponents)
    time.sleep(1)


