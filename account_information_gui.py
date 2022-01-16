from tkinter import messagebox
from tkinter import *
import json
import socket

# Colors
YELLOW = "#FFC900"
LIGHT_YELLOW = "#FFF89A"
BLUE = "#086E7D"
DARK_BLUE = "#1A5F7A"

# Fonts
AMERICANCAPTIAN = ("AmericanCaptain", "22", "normal")
ACUIRE = ("Acuire Bold", "15", "bold")
MOMCAKE = ("MomcakeBold", "10", "bold")

HOST = "127.0.0.1"
PORT = 80


class Account_Information_GUI:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        # UI
        self.window = Tk()
        self.window.title("YOUR ACCOUNT INFORMATIONS")
        self.window.geometry("300x300")
        self.window.config(bg=YELLOW, padx=20, pady=20)

        # Label
        self.label_username = Label(text=f"Username : {self.username}", font=ACUIRE, bg=YELLOW,
                                    highlightthickness=0,
                                    fg="black")
        self.label_password = Label(text=f"Password : {self.password}", font=ACUIRE, bg=YELLOW,
                                    highlightthickness=0,
                                    fg="black")
        self.label_musiccloud = Label(text="Music Cloud", font=AMERICANCAPTIAN, bg=YELLOW, highlightthickness=0,
                                      fg="black")

        # Canvas
        self.canvas_logo = Canvas(width=125, height=100)
        img_logo = PhotoImage(file="music_small.png")
        self.canvas_logo.create_image(65, 50, image=img_logo)
        self.canvas_logo.config(bg=YELLOW, highlightthickness=0)
        self.canvas_logo.bind("<Button-1>", self.go_to_sign_in_page)

        # Buttons
        self.sign_in_btn = Button(text="Sign In", width=25, height=1,
                                  command=self.go_to_sign_in_page, bg=BLUE,
                                  fg=LIGHT_YELLOW, font=("MomcakeBold", "12", "bold"))

        # Giving positions
        self.canvas_logo.grid(column=0, row=0)
        self.label_musiccloud.grid(column=0, row=1, pady=10)
        self.label_username.grid(column=0, row=2, pady=10)
        self.label_password.grid(column=0, row=3, pady=10)
        self.sign_in_btn.grid(column=0, row=4, pady=10)

        self.window.mainloop()

    def go_to_sign_in_page(self):
        import logging_in_gui
        self.window.destroy()
        logging_in_gui.Logging_In_GUI()

Account_Information_GUI("")