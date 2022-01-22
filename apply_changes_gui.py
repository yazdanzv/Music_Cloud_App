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

HOST = "127.0.0.1"
PORT = 80


class Apply_Changes_GUI:
    def __init__(self, firstname, lastname, email, phone, username, password, old_firstname, old_lastname, old_email,
                 old_phone, old_password):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.phone = phone
        self.username = username
        self.password = password
        self.old_firstname = old_firstname
        self.old_lastname = old_lastname
        self.old_email = old_email
        self.old_phone = old_phone
        self.old_password = old_password
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((HOST, PORT))
        print(self.old_firstname + "3333")
        print(self.firstname + "3333")

        # UI
        self.window = Tk()
        self.window.title("Music Cloud")
        self.window.geometry("290x280")
        self.window.config(bg=YELLOW, padx=20, pady=20)
        self.window.bind("<Destroy>", self.destroy)

        # Canvas
        self.canvas_logo = Canvas(width=125, height=100)
        img_logo = PhotoImage(file="music_small.png")
        self.canvas_logo.create_image(65, 50, image=img_logo)
        self.canvas_logo.config(bg=YELLOW, highlightthickness=0)

        # Labels
        self.question_label = Label(text="Are you sure ?", font=AMERICANCAPTIAN, bg=YELLOW, highlightthickness=0)

        # Buttons
        self.yes_btn = Button(text="Yes", width=8, height=1, command=self.yes_clicked, bg=BLUE,
                              fg="black", font=("MomcakeBold", "14", "bold"))
        self.no_btn = Button(text="No", width=8, height=1, command=self.no_clicked, bg=BLUE,
                             fg="black", font=("MomcakeBold", "14", "bold"))

        # Giving position
        self.canvas_logo.grid(column=0, row=0, columnspan=2, pady=10)
        self.question_label.grid(column=0, row=1, columnspan=2, pady=10)
        self.yes_btn.grid(column=0, row=2, padx=10, pady=10)
        self.no_btn.grid(column=1, row=2, padx=10, pady=10)

        self.window.mainloop()

    def destroy(self, event):
        self.s.close()
        print("socket in apply changes page closed")
        pass

    def yes_clicked(self):
        import changing_infos_gui
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.connect((HOST, PORT))
        except:
            pass
        firstname = self.firstname
        lastname = self.lastname
        email = self.email
        phone = self.phone
        username = self.username
        password = self.password
        data = {username: {"firstname": firstname,
                           "lastname": lastname,
                           "email": email,
                           "phone": phone,
                           "password": password}}
        info = json.dumps(data)
        info = info + "4"
        self.s.send(info.encode())
        try:
            self.window.destroy()
        except:
            pass
        changing_infos_gui.Changing_Infos_GUI(firstname, lastname, email, phone, username, password)
        self.s.close()

    def no_clicked(self):
        import changing_infos_gui
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.connect((HOST, PORT))
        except:
            pass
        self.s.send((self.username + "6").encode())
        data = self.s.recv(1024).decode()
        info: dict = json.loads(data)
        username = self.username
        firstname = info["firstname"]
        lastname = info["lastname"]
        email = info["email"]
        phone = info["phone"]
        password = info["password"]
        try:
            self.window.destroy()
        except:
            pass
        changing_infos_gui.Changing_Infos_GUI(firstname, lastname, email, phone, username, password)
        self.s.close()


