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
MOMCAKE = ("MomcakeBold", "8", "bold")

HOST = "127.0.0.1"
PORT = 80


class Verify_GUI:
    def __init__(self, code, user_email):
        self.code = code
        self.user_email = user_email
        # UI
        self.window = Tk()
        self.window.title("Music Cloud")
        self.window.geometry("300x300")
        self.window.config(bg=YELLOW, padx=20, pady=20)

        # Canvas
        self.canvas_logo = Canvas(width=125, height=100)
        img_logo = PhotoImage(file="music_small.png")
        self.canvas_logo.create_image(65, 50, image=img_logo)
        self.canvas_logo.config(bg=YELLOW, highlightthickness=0)
        self.canvas_logo.bind("<Button-1>", self.back_clicked)

        # Edit Text
        self.code_entry = Entry(width=40, bg=LIGHT_YELLOW, disabledbackground=LIGHT_YELLOW)
        self.code_entry.insert(0, "Security Code")
        self.code_entry["state"] = "disable"
        self.code_entry.bind("<Button-1>", self.enable_entry)

        # Buttons
        self.verify_btn = Button(text="Verify", width=25, height=1,
                                 command=self.verify_clicked, bg=BLUE,
                                 fg=LIGHT_YELLOW, font=("MomcakeBold", "12", "bold"))

        # Labels
        self.label_resend_email = Label(text="Resent email", font=MOMCAKE, bg=YELLOW, highlightthickness=0,
                                  fg="black")
        self.label_resend_email.bind("<Button-1>", self.resent_email_clicked)
        self.label_musiccloud = Label(text="Music Cloud", font=AMERICANCAPTIAN, bg=YELLOW, highlightthickness=0,
                                      fg="black")
        self.label_musiccloud.bind("<Button-1>", self.back_clicked)

        # Giving positions
        self.canvas_logo.grid(column=0, row=0)
        self.label_musiccloud.grid(column=0, row=1, pady=10)
        self.code_entry.grid(column=0, row=2, pady=5)
        self.label_resend_email.grid(column=0, row=3, pady=5)
        self.verify_btn.grid(column=0, row=4, pady=5)

        self.window.mainloop()

    def enable_entry(self, event):
        self.code_entry["state"] = "normal"
        self.code_entry.delete(0, END)

    def verify_clicked(self):
        import account_information_gui
        if self.code == self.code_entry.get():
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((HOST, PORT))
            s.send(f"{self.user_email}8".encode())
            data = s.recv(1024).decode()
            print(data)
            info = json.loads(data)
            username = info["username"]
            password = info["password"]
            s.close()
            self.window.destroy()
            account_information_gui.Account_Information_GUI(username, password)
        else:
            messagebox.showerror(title="ERROE", message="Security Code is not correct")
            self.code_entry.focus_force()

    def resent_email_clicked(self, event):
        print("resent entered")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        s.send((self.user_email + "9").encode())
        ans = s.recv(1024).decode()
        print(ans)
        if ans[-1] == "1":
            self.code = ans[0:-1]
            messagebox.showinfo(title="SENT", message="Email sent again")
        else:
            raise Exception("email didn't send !!!")

    def back_clicked(self, event):
        import logging_in_gui
        self.window.destroy()
        logging_in_gui.Logging_In_GUI()

# Verify_GUI("111")