from tkinter import *
from tkinter import messagebox
import json



# Colors
YELLOW = "#FFC900"
LIGHT_YELLOW = "#FFF89A"
BLUE = "#086E7D"
DARK_BLUE = "#1A5F7A"

# Fonts
AMERICANCAPTIAN = ("AmericanCaptain", "16", "normal")
ACUIRE = ("Acuire Bold", "15", "bold")
MOMCAKE = ("MomcakeBold", "10", "bold")
STEAMED = ("Steamed DEMO", "12", "normal")


class Setting_GUI:
    def __init__(self, firstname: str, lastname: str, email: str, phone: str, username: str, password: str):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.phone = phone
        self.username = username
        self.password = password

        # GUI
        self.window = Tk()
        self.window.geometry("350x300")
        self.window.title("User Setting")
        self.window.config(bg=YELLOW, padx=10, pady=10)

        # Buttons
        self.back_btn = Button(text="Back", bg=BLUE, font=ACUIRE, fg=LIGHT_YELLOW, command=self.go_back)
        self.log_out_btn = Button(text="Log out", bg=BLUE, font=ACUIRE, fg=LIGHT_YELLOW, width=10, command=self.log_out)
        self.user_datas_btn = Button(text="User Datas", bg=BLUE, font=ACUIRE, fg=LIGHT_YELLOW, width=10, command=self.user_datas)

        # Canvas
        self.canvas_avatar = Canvas(width=100, height=75)
        img_avatar = PhotoImage(file="Avatar.png")
        self.canvas_avatar.create_image(50, 37, image=img_avatar)
        self.canvas_avatar.config(bg=YELLOW, highlightthickness=0)

        # Labels
        self.name_label = Label(text=f"{self.firstname} {self.lastname}", font=AMERICANCAPTIAN, bg=YELLOW, highlightthickness=0)

        # Giving position
        self.back_btn.grid(column=0, row=0, pady=30)
        self.name_label.grid(column=1, row=0, columnspan=2, pady=30, padx=10)
        self.canvas_avatar.grid(column=3, row=0, pady=30)
        self.log_out_btn.grid(column=1, row=1, columnspan=2, pady=10)
        self.user_datas_btn.grid(column=1, row=2, columnspan=2, pady=10)

        self.window.mainloop()

    def go_back(self):
        import using_gui
        firstname = self.firstname
        lastname = self.lastname
        email = self.email
        phone = self.phone
        username = self.username
        password = self.password
        try:
            self.window.destroy()
        except:
            pass
        using_gui.Using_GUI(firstname, lastname, email, phone, username, password)

    def user_datas(self):
        import changing_infos_gui
        firstname = self.firstname
        lastname = self.lastname
        email = self.email
        phone = self.phone
        username = self.username
        password = self.password
        try:
            self.window.destroy()
        except:
            pass
        changing_infos_gui.Changing_Infos_GUI(firstname, lastname, email, phone, username, password)

    def log_out(self):
        import logging_in_gui
        try:
            self.window.destroy()
        except:
            pass
        logging_in_gui.Logging_In_GUI()


