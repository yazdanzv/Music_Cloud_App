from tkinter import messagebox
from tkinter import *
import json
import socket
import re

# Colors
YELLOW = "#FFC900"
LIGHT_YELLOW = "#FFF89A"
BLUE = "#086E7D"
DARK_BLUE = "#1A5F7A"

# Fonts
AMERICANCAPTIAN = ("AmericanCaptain", "27", "bold")
ACUIRE = ("Acuire Bold", "15", "bold")
MOMCAKE = ("MomcakeBold", "10", "bold")


HOST = "127.0.0.1"
PORT = 80



class Logging_In_GUI:
    username = ""
    firstname = ""
    lastname = ""
    phone = ""
    email = ""
    password = ""

    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((HOST, PORT))
        self.window = Tk()
        self.window.title("Music Cloud")
        self.window.geometry("500x800")
        self.window.config(bg=YELLOW, padx=20, pady=20)
        self.window.bind("<Destroy>", self.destroy)

        # Canvas for Logo
        img = PhotoImage(file="music.png")
        self.canvas = Canvas(width=300, height=250)
        self.canvas.create_image(150, 125, image=img)
        self.canvas.config(bg=YELLOW, highlightthickness=0)

        # Labels
        # Sign in
        self.label_title = Label(text="Music Cloud", font=AMERICANCAPTIAN, bg=YELLOW, highlightthickness=0)
        self.label_username = Label(text="Username", font=MOMCAKE, bg=YELLOW, highlightthickness=0)
        self.label_password = Label(text="Password", font=MOMCAKE, bg=YELLOW, highlightthickness=0)
        # Sign up
        self.label_email = Label(text="Email", font=MOMCAKE, bg=YELLOW, highlightthickness=0)
        self.label_firstname = Label(text="First Name", font=MOMCAKE, bg=YELLOW, highlightthickness=0)
        self.label_lastname = Label(text="Last Name", font=MOMCAKE, bg=YELLOW, highlightthickness=0)
        self.label_confirm = Label(text="Confirm", font=MOMCAKE, bg=YELLOW, highlightthickness=0)
        self.label_phone = Label(text="Phone number", font=MOMCAKE, bg=YELLOW, highlightthickness=0)

        # Edit Text
        self.username_entry = Entry(width=40)
        self.password_entry = Entry(width=40)
        self.firstname_entry = Entry(width=40)
        self.last_name_entry = Entry(width=40)
        self.confirm_entry = Entry(width=40)
        self.email_entry = Entry(width=40)
        self.phone_entry = Entry(width=40)

        # Radio buttons
        self.user_ans = StringVar()
        self.sign_in_rbtn = Radiobutton(text="Sign in", value="Sign in", variable=self.user_ans, font=ACUIRE,
                                        bg=LIGHT_YELLOW, fg="black", command=self.sign_in_radioclicked,
                                        indicator=0)
        self.sign_up_rbtn = Radiobutton(text="Sign up", value="Sign up", variable=self.user_ans, font=ACUIRE,
                                        bg=LIGHT_YELLOW, fg="black", command=self.sign_up_radioclicked, indicator=0)

        # Buttons
        # Sign in
        self.sign_in_btn = Button(text="Sign in", width=25, height=1, command=self.sign_in_btn_clicked, bg=BLUE,
                                  fg="black", font=("MomcakeBold", "14", "bold"))
        # Sign up
        self.sign_up_btn = Button(text="Sign up", width=25, height=1, command=self.sign_up_btn_clicked, bg=BLUE,
                                  fg="black", font=("MomcakeBold", "14", "bold"))

        # Giving position
        self.canvas.grid(column=1, row=0, columnspan=2)
        self.label_title.grid(column=1, row=1, columnspan=2)
        self.sign_in_rbtn.grid(column=1, row=2, padx=5, pady=20)
        self.sign_up_rbtn.grid(column=2, row=2, padx=5, pady=20)
        self.label_username.grid(column=0, row=3, padx=5, pady=10)
        self.username_entry.grid(column=1, row=3, columnspan=3)
        self.label_password.grid(column=0, row=4, padx=5, pady=10)
        self.password_entry.grid(column=1, row=4, columnspan=3)
        self.sign_in_btn.grid(column=1, row=5, columnspan=3, pady=22)

        self.sign_in_rbtn["state"] = "disable"

        self.window.mainloop()

    def destroy(self, event):
        self.s.close()
        print("socket in log in page closed")
        pass

    def sign_up_sendtoserver(self):
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.connect((HOST, PORT))
        except:
            pass
        new_data = {self.username_entry.get(): {"firstname": self.firstname_entry.get(),
                                                "lastname": self.last_name_entry.get(),
                                                "email": self.email_entry.get(),
                                                "phone": self.phone_entry.get(),
                                                "password": self.password_entry.get(),
                                                "musics": [],
                                                }}
        data = json.dumps(new_data)
        self.s.send((data + "1").encode())

        code = self.s.recv(1024).decode()
        print(code)
        if code == "1":
            messagebox.showerror(title="ERROR", message="this username exists")
            self.username_entry.focus_force()
        elif code == "0":
            messagebox.showinfo(title="You signed up successfully", message="You can sign in now")
            self.sign_in_rbtn.focus_force()
        elif code == "2":
            messagebox.showerror(title="ERROR", message="This Email has already registered")
            self.email_entry.focus_force()
        elif code == "3":
            messagebox.showerror(title="ERROR", message="This phone number already registered")
            self.phone_entry.focus_force()
        else:
            raise Exception("Code is incorrect !!!")
        self.s.close()


    def sign_in_sendtoserver(self):
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.connect((HOST, PORT))
        except:
            pass
        info = {"username": self.username_entry.get(), "password": self.password_entry.get()}
        data = json.dumps(info)
        self.s.send((data + "3").encode())
        data_rcv = self.s.recv(1024).decode()
        if data_rcv == "2":
            return 2
        elif data_rcv == "3":
            return 3
        else:
            data_rcv = json.loads(data_rcv)
            self.username = self.username_entry.get()
            self.password = self.password_entry.get()
            self.firstname = data_rcv["firstname"]
            self.lastname = data_rcv["lastname"]
            self.email = data_rcv["email"]
            self.phone = data_rcv["phone"]
            return 1
        self.s.close()

    def goto_using_page(self):
        import using_gui
        firstname = self.firstname
        lastname = self.lastname
        email = self.email
        username = self.username
        password = self.password
        phone = self.phone
        self.window.destroy()
        using_gui.Using_GUI(firstname, lastname, email, phone, username, password)

    def sign_in_radioclicked(self):
        self.sign_in_rbtn["state"] = "disable"
        self.sign_up_rbtn["state"] = "normal"
        # Delete the previous arrangement
        self.label_firstname.grid_forget()
        self.label_lastname.grid_forget()
        self.label_username.grid_forget()
        self.label_email.grid_forget()
        self.label_password.grid_forget()
        self.label_confirm.grid_forget()
        self.label_phone.grid_forget()
        self.phone_entry.grid_forget()
        self.firstname_entry.grid_forget()
        self.last_name_entry.grid_forget()
        self.username_entry.grid_forget()
        self.email_entry.grid_forget()
        self.password_entry.grid_forget()
        self.confirm_entry.grid_forget()
        self.sign_up_btn.grid_forget()
        # Setting the new arrangement
        self.label_username.grid(column=0, row=3, padx=5, pady=10)
        self.username_entry.grid(column=1, row=3, columnspan=3)
        self.label_password.grid(column=0, row=4, padx=5, pady=10)
        self.password_entry.grid(column=1, row=4, columnspan=3)
        self.sign_in_btn.grid(column=1, row=5, columnspan=3, pady=22)
        self.username_entry.focus_force()

    def sign_up_radioclicked(self):
        self.sign_in_rbtn["state"] = "normal"
        self.sign_up_rbtn["state"] = "disable"
        # Delete the previous arrangement
        self.username_entry.grid_forget()
        self.password_entry.grid_forget()
        self.label_password.grid_forget()
        self.label_username.grid_forget()
        self.sign_in_btn.grid_forget()
        # Setting the new arrangement
        self.label_firstname.grid(column=0, row=3, padx=5, pady=10)
        self.firstname_entry.grid(column=1, row=3, columnspan=3)
        self.label_lastname.grid(column=0, row=4, padx=5, pady=10)
        self.last_name_entry.grid(column=1, row=4, columnspan=3)
        self.label_username.grid(column=0, row=5, padx=5, pady=10)
        self.username_entry.grid(column=1, row=5, columnspan=3)
        self.label_email.grid(column=0, row=6, padx=5, pady=10)
        self.email_entry.grid(column=1, row=6, columnspan=3)
        self.label_phone.grid(column=0, row=7, padx=5, pady=10)
        self.phone_entry.grid(column=1, row=7, columnspan=3)
        self.label_password.grid(column=0, row=8, padx=5, pady=10)
        self.password_entry.grid(column=1, row=8, columnspan=3)
        self.label_confirm.grid(column=0, row=9, padx=5, pady=10)
        self.confirm_entry.grid(column=1, row=9, columnspan=3)
        self.sign_up_btn.grid(column=1, row=10, columnspan=3, pady=22)
        self.firstname_entry.focus_force()

    def sign_in_btn_clicked(self):
        if len(self.username_entry.get()) != 0 and len(self.password_entry.get()) != 0:
            flag_num = self.sign_in_sendtoserver()
            if flag_num == 1:
                self.window.after(1000, self.goto_using_page)
            elif flag_num == 2:
                messagebox.showerror(title="ERROR", message="Your password is wrong")
                self.password_entry.focus_force()
            elif flag_num == 3:
                messagebox.showerror(title="ERROR", message="You didn't signed up")
                self.sign_up_rbtn.focus_force()
        else:
            if len(self.username_entry.get()) == 0 and len(self.password_entry.get()) == 0:
                messagebox.showerror(title="ERROR", message="You didn't fill the sections")
                self.username_entry.focus_force()
            elif len(self.username_entry.get()) == 0 and len(self.password_entry.get()) != 0:
                messagebox.showerror(title="ERROR", message="You didn't entered your username")
                self.username_entry.focus_force()
            elif len(self.username_entry.get()) != 0 and len(self.password_entry.get()) == 0:
                messagebox.showerror(title="ERROR", message="You didn't entered your password")
                self.password_entry.focus_force()

    def sign_up_btn_clicked(self):
        # Saving the user datas

        if len(self.username_entry.get()) != 0 and len(self.firstname_entry.get()) != 0 and len(
                self.last_name_entry.get()) != 0 and len(self.password_entry.get()) != 0 and len(
                self.email_entry.get()) != 0 and len(self.phone_entry.get()) != 0:
            if self.password_entry.get() == self.confirm_entry.get():
                if self.phone_number_checker(self.phone_entry.get()):
                    if self.email_checker(self.email_entry.get()):
                        self.window.after(500, self.sign_up_sendtoserver)
                    else:
                        messagebox.showerror(title="ERROR", message="Email is not validate")
                        self.email_entry.focus_force()
                else:
                    messagebox.showerror(title="ERROR", message="Phone number is not validate")
                    self.phone_entry.focus_force()
            else:
                messagebox.showerror(title="ERROR", message="You didn't confirm your password correctly")
        else:
            messagebox.showerror(title="ERROR", message="Complete all the sections")

    def phone_number_checker(self, phone):
        if re.match("^09[0-9]{9}$", phone):
            return True
        return False

    def email_checker(self, email):
        if re.match(".{1,30}@.{1,20}\..{1,10}", email):
            return True
        return False


# Logging_In_GUI()
