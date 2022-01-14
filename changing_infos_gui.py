from tkinter import *
from tkinter import messagebox
import json
import socket

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


class Changing_Infos_GUI:
    def __init__(self, firstname, lastname, email, phone, username, password):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.phone = phone
        self.username = username
        self.password = password
        self.old_firstname = firstname
        self.old_lastname = lastname
        self.old_email = email
        self.old_phone = phone
        self.old_password = password
        print(self.firstname + "222")
        print(self.old_firstname + "222")

        # UI
        self.window = Tk()
        self.window.title("User Informations")
        self.window.geometry("500x500")
        self.window.config(bg=YELLOW, padx=20, pady=20)

        # Canvas
        self.canvas_logo = Canvas(width=125, height=100)
        img_logo = PhotoImage(file="music_small.png")
        self.canvas_logo.create_image(65, 50, image=img_logo)
        self.canvas_logo.config(bg=YELLOW, highlightthickness=0)

        self.canvas_avatar = Canvas(width=75, height=75)
        img_avatar = PhotoImage(file="Avatar.png")
        self.canvas_avatar.create_image(37, 37, image=img_avatar)
        self.canvas_avatar.config(bg=YELLOW, highlightthickness=0)

        # Labels
        self.label_firstname = Label(text="Firstname : ", font=MOMCAKE, bg=YELLOW, highlightthickness=0)
        self.label_lastname = Label(text="Lastname : ", font=MOMCAKE, bg=YELLOW, highlightthickness=0)
        self.label_email = Label(text="Email : ", font=MOMCAKE, bg=YELLOW, highlightthickness=0)
        self.label_phone = Label(text="Phone number : ", font=MOMCAKE, bg=YELLOW, highlightthickness=0)
        self.label_password = Label(text="Password : ", font=MOMCAKE, bg=YELLOW, highlightthickness=0)

        # Edit Texts
        self.firstname_entry = Entry(width=40)
        self.firstname_entry.insert(0, self.firstname)
        self.firstname_entry.config(bg=LIGHT_YELLOW, highlightthickness=0)
        self.last_name_entry = Entry(width=40)
        self.last_name_entry.insert(0, self.lastname)
        self.last_name_entry.config(bg=LIGHT_YELLOW, highlightthickness=0)
        self.email_entry = Entry(width=40)
        self.email_entry.insert(0, self.email)
        self.email_entry.config(bg=LIGHT_YELLOW, highlightthickness=0)
        self.phone_entry = Entry(width=40)
        self.phone_entry.insert(0, self.phone)
        self.phone_entry.config(bg=LIGHT_YELLOW, highlightthickness=0)
        self.password_entry = Entry(width=40)
        self.phone_entry.insert(0, self.password)
        self.password_entry.config(bg=LIGHT_YELLOW, highlightthickness=0)
        self.firstname_entry.bind('<KeyRelease>', self.enable_apply_btn)
        self.last_name_entry.bind('<KeyRelease>', self.enable_apply_btn)
        self.email_entry.bind('<KeyRelease>', self.enable_apply_btn)
        self.phone_entry.bind('<KeyRelease>', self.enable_apply_btn)
        self.password_entry.bind('<KeyRelease>', self.enable_apply_btn)

        # Buttons
        self.back_btn = Button(text="Back", bg=BLUE, font=ACUIRE, fg=LIGHT_YELLOW, command=self.go_back)
        self.apply_btn = Button(text="Apply", bg=BLUE, font=ACUIRE, fg=LIGHT_YELLOW, command=self.apply, width=30)
        self.apply_btn["state"] = "disable"

        # Giving position
        self.back_btn.grid(column=0, row=0, pady=10)
        self.canvas_logo.grid(column=1, row=0, columnspan=2, pady=10, padx=10)
        self.canvas_avatar.grid(column=3, row=0, columnspan=2, pady=10)
        self.label_firstname.grid(column=1, row=1, pady=10, padx=5)
        self.firstname_entry.grid(column=2, row=1, columnspan=2, pady=10, padx=5)
        self.label_lastname.grid(column=1, row=2, pady=10, padx=5)
        self.last_name_entry.grid(column=2, row=2, columnspan=2, pady=10, padx=5)
        self.label_email.grid(column=1, row=3, pady=10, padx=5)
        self.email_entry.grid(column=2, row=3, columnspan=2, pady=10, padx=5)
        self.label_phone.grid(column=1, row=4, pady=10, padx=5)
        self.phone_entry.grid(column=2, row=4, columnspan=2, pady=10, padx=5)
        self.label_password.grid(column=1, row=5, pady=10, padx=5)
        self.password_entry.grid(column=2, row=5, columnspan=2, pady=10, padx=5)
        self.apply_btn.grid(column=1, row=6, columnspan=3, pady=20)

        self.window.mainloop()

    def go_back(self):
        import setting_gui
        firstname = self.old_firstname
        lastname = self.old_lastname
        email = self.old_email
        phone = self.old_phone
        username = self.username
        password = self.old_password
        try:
            self.window.destroy()
        except:
            pass
        print(firstname + "1")
        print(lastname + "1")
        setting_gui.Setting_GUI(firstname, lastname, email, phone, username, password)

    def apply(self):
        import apply_changes_gui
        if len(self.password_entry.get()) != 0:
            password = self.password_entry.get()
        else:
            password = self.old_password
        old_firstname = self.old_firstname
        old_lastname = self.old_lastname
        old_email = self.old_email
        old_phone = self.old_phone
        old_password = self.old_password
        firstname = self.firstname_entry.get()
        lastname = self.last_name_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        username = self.username
        self.window.destroy()
        apply_changes_gui.Apply_Changes_GUI(firstname, lastname, email, phone, username, password, old_firstname, old_lastname, old_email, old_phone, old_password)

    def enable_apply_btn(self, event):
        self.old_firstname = self.firstname_entry.get()
        self.old_lastname = self.last_name_entry.get()
        self.old_email = self.email_entry.get()
        self.old_phone = self.phone_entry.get()
        self.old_password = self.password_entry.get()
        if self.firstname_entry.get() != self.firstname or self.last_name_entry.get() != self.lastname or self.email_entry.get() != self.email \
                or self.phone_entry.get() != self.phone:
            self.apply_btn["state"] = "normal"
        elif len(self.password_entry.get()) != 0 and self.password_entry.get() != self.password:
                self.apply_btn["state"] = "normal"
        else:
            self.apply_btn["state"] = "disable"

# Changing_Infos_GUI("yazdan", "zandiyevakili", "yazdanzv.1378@gmail.com", "09354416622", "yazdanzv", "yanik1387")