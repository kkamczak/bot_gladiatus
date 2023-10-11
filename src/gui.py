import sys
import tkinter
from tkinter import Tk, Label, Button
import globals as GLOBALS
from functions import puts


class Gui:
    def __init__(self):
        self.root = Tk()
        self.root.title('Gladiatus Bot by kkamczak')
        self.root.geometry("600x400")

        self.level = 0
        self.paused = False
        self.do_expeditions = True
        self.do_dungeons = True
        self.do_cp = True
        self.information = ''

        self.exit = False

        self.load_globals()

        self.configure_gui(self.root)

        self.update_gui()

        self.run()

    def update(self):
        print("Jajko")
        self.root.after(2000, self.update)
    def load_globals(self):

        self.level = GLOBALS.LEVEL
        self.paused = GLOBALS.PAUSED
        self.do_expeditions = GLOBALS.DO_EXPEDITIONS
        self.do_dungeons = GLOBALS.DO_DUNGEONS
        self.do_cp = GLOBALS.DO_CP
        self.informations = GLOBALS.INFORMATIONS

    def save_globals(self):

        GLOBALS.PAUSED = self.paused
        GLOBALS.DO_EXPEDITIONS = self.do_expeditions
        GLOBALS.DO_DUNGEONS = self.do_dungeons
        GLOBALS.DO_CP = self.do_cp


    def configure_gui(self, root):

        # Nagłówki:
        self.label_1 = Label(root, text="Gladiatus Bot", font=40, fg="blue")
        self.label_1.pack(pady=5)

        self.label_2 = Label(root, text=("Aktualny level: " + str(self.level)), font=30, fg="blue")
        self.label_2.pack(pady=5)

        if not self.paused:
            self.label_3 = Label(root, text=("Bot jest uruchomiony"), font=30, fg="blue")
        else:
            self.label_3 = Label(root, text=("Bot jest wstrzymany"), font=30, fg="blue")

        self.label_3.pack(pady=5)



        # Przyciski:
        button_width = 25

        self.expedition_button = Button(root, text=("Ekspedycje: " + str(self.do_expeditions)), width=button_width,
                                   command=self.change_expedition_status, bg="#87ed7b")
        self.expedition_button.pack(pady=5)

        self.dungeon_button = Button(root, text=("Lochy: " + str(self.do_dungeons)), width=button_width,
                                command=self.change_dungeon_status, bg="#87ed7b")
        self.dungeon_button.pack(pady=5)

        self.cp_button = Button(root, text=("Circus Provinciarum: " + str(self.do_cp)), width=button_width,
                           command=self.change_cp_status, bg="#87ed7b")
        self.cp_button.pack(pady=5)

        self.pause_button = Button(root, text=("Zapauzuj program"), width=button_width,
                              command = self.change_pause_status, bg="#87ed7b")
        self.pause_button.pack(pady=5)

        self.exit_button = Button(root, text=("Wyjdz z programu"), width=button_width,
                                   command=self.stop_program, bg="#87ed7b")
        self.exit_button.pack(pady=5)

        #Informations:
        self.label_4 = Label(root, text=(self.informations[0]), font=('Helvatical bold',10), fg="blue")
        self.label_4.pack(pady=5)

        self.label_5 = Label(root, text=(self.informations[1]), font=('Helvatical bold', 10), fg="blue")
        self.label_5.pack(pady=5)

        self.label_6 = Label(root, text=(self.informations[2]), font=('Helvatical bold', 10), fg="blue")
        self.label_6.pack(pady=5)

    def update_gui(self):
        self.load_globals()

        self.label_2.config(text=("Aktualny level: " + str(self.level)))
        self.label_4.config(text=(self.informations[0]))
        self.label_5.config(text=(self.informations[1]))
        self.label_6.config(text=(self.informations[2]))

        self.exit_program()

        self.root.after(500, self.update_gui)

    def change_expedition_status(self):
        self.load_globals()

        if self.do_expeditions:
            self.do_expeditions = False
            color = "#f74a6a"
        else:
            self.do_expeditions = True
            color = "#87ed7b"
        self.expedition_button.config(text=("Ekspedycje: " + str(self.do_expeditions)), bg=color)

        self.save_globals()
        self.update_gui()

    def change_dungeon_status(self):
        self.load_globals()

        if self.do_dungeons:
            self.do_dungeons = False
            color = "#f74a6a"
        else:
            self.do_dungeons = True
            color = "#87ed7b"
        self.dungeon_button.config(text=("Lochy: " + str(self.do_dungeons)), bg=color)

        self.save_globals()
        self.update_gui()

    def change_cp_status(self):

        if self.do_cp:
            self.do_cp = False
            color = "#f74a6a"
        else:
            self.do_cp = True
            color = "#87ed7b"
        self.cp_button.config(text=("Circus Provinciarum: " + str(self.do_cp)), bg=color)

        self.save_globals()

    def change_pause_status(self):
        self.load_globals()

        if self.paused:
            self.paused = False
            self.label_3.config(text="Bot jest uruchomiony")
            self.pause_button.config(text="Zapauzuj program", bg="#87ed7b")
        else:
            self.paused = True
            self.label_3.config(text="Bot jest wstrzymany")
            self.pause_button.config(text="Wznów program", bg="#f74a6a")

        self.save_globals()

    def stop_program(self):
        GLOBALS.CLOSING = True
        self.exit_button.config(bg="#f74a6a")
    def exit_program(self):

        if GLOBALS.CLOSING:
            self.label_3.config(text="Bot zaraz zostanie wyłączony")
            self.expedition_button.config(state = tkinter.DISABLED, bg="#f74a6a")
            self.dungeon_button.config(state=tkinter.DISABLED, bg="#f74a6a")
            self.cp_button.config(state=tkinter.DISABLED, bg="#f74a6a")
            self.pause_button.config(state=tkinter.DISABLED, bg="#f74a6a")
            self.exit_button.config(state=tkinter.DISABLED, bg="#f74a6a")
        if GLOBALS.CLOSING and not GLOBALS.RUNNING:
            sys.exit()

    def run(self):
        self.root.mainloop()