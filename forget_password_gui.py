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


class Password_Forget_GUI:

    def __init__(self):
        # UI
        self.window = Tk()
        self.window.title("Music Cloud")
        self.window.geometry("300x300")
        self.window.config(bg=YELLOW, padx=20, pady=20)

        # Labels
        self.label_musiccloud = Label(text="Music Cloud", font=AMERICANCAPTIAN, bg=YELLOW, highlightthickness=0, fg="black")
        self.label_musiccloud.bind("<Button-1>", self.back_clicked)

        # Edit Texts
        self.entry_username = Entry(width=40, bg=LIGHT_YELLOW, disabledbackground=LIGHT_YELLOW)
        self.entry_username.insert(0, "Username or Email")
        self.entry_username["state"] = "disable"
        self.entry_username.bind("<Button-1>", self.enable_entry)
        self.entry_username.bind("<FocusOut>", self.disable_entry)
        self.entry_username.bind("<KeyRelease>", self.enable_btn)

        # Canvas
        self.canvas_logo = Canvas(width=125, height=100)
        img_logo = PhotoImage(file="music_small.png")
        self.canvas_logo.create_image(65, 50, image=img_logo)
        self.canvas_logo.config(bg=YELLOW, highlightthickness=0)
        self.canvas_logo.bind("<Button-1>", self.back_clicked)

        # Buttons
        self.retreive_password_btn = Button(text="Reterive my password", width=25, height=1,
                                            command=self.retreive_password_clicked, bg=BLUE,
                                            fg=LIGHT_YELLOW, font=("MomcakeBold", "12", "bold"))
        self.retreive_password_btn["state"] = "disable"

        # Giving position
        self.canvas_logo.grid(column=0, row=0)
        self.label_musiccloud.grid(column=0, row=1, pady=10)
        self.entry_username.grid(column=0, row=2, pady=10)
        self.retreive_password_btn.grid(column=0, row=3, pady=10)

        self.window.mainloop()

    def retreive_password_clicked(self):
        import verify_gui
        user_or_email: str = self.entry_username.get()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        s.send((user_or_email + "7").encode())
        security_code = s.recv(1024).decode()
        print(security_code)
        print(type(security_code))
        if security_code[-1] == "1":
            security_code = security_code[0:-1]
            username_email = self.entry_username.get()
            self.window.destroy()
            verify_gui.Verify_GUI(security_code, username_email)
        else:
            messagebox.showerror(title="ERROR", message="this email or username not found")

    def back_clicked(self):
        import logging_in_gui
        self.window.destroy()
        logging_in_gui.Logging_In_GUI()

    def enable_btn(self, event):
        if len(self.entry_username.get()) != 0:
            self.retreive_password_btn["state"] = "normal"
        elif len(self.entry_username.get()) == 0:
            self.retreive_password_btn["state"] = "disable"

    def enable_entry(self, event):
        self.entry_username["state"] = "normal"
        self.entry_username.delete(0, END)

    def disable_entry(self, event):
        if self.entry_username.get() == "":
            self.entry_username.insert(0, "Username or Email")
            self.entry_username["state"] = "disable"


