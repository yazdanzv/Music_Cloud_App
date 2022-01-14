from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import json
import os
import socket

# Colors
YELLOW = "#FFC900"
LIGHT_YELLOW = "#FFF89A"
BLUE = "#086E7D"
DARK_BLUE = "#1A5F7A"

# Fonts
AMERICANCAPTIAN = ("AmericanCaptain", "10", "normal")
ACUIRE = ("Acuire Bold", "15", "bold")
MOMCAKE = ("MomcakeBold", "10", "bold")
STEAMED = ("Steamed DEMO", "12", "normal")

HOST = "127.0.0.1"
PORT = 80


class Using_GUI:
    def __init__(self, fname: str, lname: str, email: str, phone: str, username: str, password: str):
        # Setting the class variables
        global folder_btn_clicked
        self.firstname = fname
        self.lastname = lname
        self.email = email
        self.phone = phone
        self.password = password
        self.username = username
        self.music = ""
        self.add_music = ""
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((HOST, PORT))

        # Creating the UI
        self.window = Tk()
        self.window.title("Music Cloud")
        self.window.geometry("460x520")
        self.window.config(bg=YELLOW, padx=20, pady=20)
        self.window.bind("<Destroy>", self.destroy)

        # Canvas

        self.canvas_logo = Canvas(width=125, height=100)
        img_logo = PhotoImage(file="music_small.png")
        self.canvas_logo.create_image(65, 50, image=img_logo)
        self.canvas_logo.config(bg=YELLOW, highlightthickness=0)

        self.canvas_avatar = Canvas(width=100, height=75)
        img_avatar = PhotoImage(file="Avatar.png")
        self.canvas_avatar.create_image(50, 37, image=img_avatar)
        self.canvas_avatar.config(bg=YELLOW, highlightthickness=0)

        self.canvas_avatar.bind('<Button-1>', self.goto_setting)

        # Labels
        self.label_name = Label(text=f"{self.firstname} {self.lastname}", font=STEAMED, fg="black", bg=YELLOW,
                                highlightthickness=0)
        self.label_save = Label(text="Select your path to save", font=MOMCAKE, fg="black", bg=YELLOW,
                                highlightthickness=0)

        # Buttons
        self.download_btn = Button(text="Download", bg=BLUE, font=ACUIRE, fg=LIGHT_YELLOW,
                                   command=self.download_btn_clicked, width=15)
        self.download_btn["state"] = "disable"

        # Search Box
        # -------------------------------------------------------
        def on_keyrelease(event):
            # get text from entry
            value = event.widget.get()
            value = value.strip().lower()

            # get data from test_list
            if value == '':
                data = test_list
            else:
                data = []
                for item in test_list:
                    if value in item.lower():
                        data.append(item)

                        # update data in listbox
            listbox_update(data)

        def listbox_update(data):
            # delete previous data
            self.listbox.delete(0, 'end')

            # sorting data
            data = sorted(data, key=str.lower)

            # put new data
            for item in data:
                self.listbox.insert('end', item)

        def on_select(event):
            # display element selected on list
            self.search_entry["state"] = "normal"
            self.music = event.widget.get(event.widget.curselection())
            print(self.music)
            self.search_entry.insert(0, self.music)

        def on_click(event):
            self.search_entry.configure(state=NORMAL)
            self.search_entry.delete(0, END)

            # make the callback only work once
            self.search_entry.unbind('<Button-1>', on_click_id)

        test_list = list(os.walk("./Music Bank"))[0][2]
        self.search_entry = Entry(width=30)
        self.search_entry.config(bg=LIGHT_YELLOW, highlightthickness=0, disabledbackground=LIGHT_YELLOW)
        self.search_entry.bind('<KeyRelease>', on_keyrelease)
        self.listbox = Listbox()
        self.listbox.config(width=30, height=4, bg=LIGHT_YELLOW, highlightthickness=0)
        self.search_entry.insert(0, "Search your music")
        self.search_entry.configure(state=DISABLED)
        on_click_id = self.search_entry.bind('<Button-1>', on_click)
        # self.listbox.bind('<Double-Button-1>', on_select)
        self.listbox.bind('<<ListboxSelect>>', on_select)
        listbox_update(test_list)

        # --------------------------------------------------------------------------------------------------------

        # Folder Selector
        # --------------------------------------------------------------------------------------------------------
        def folder_btn_clicked():
            self.directory = filedialog.askdirectory()
            self.label_save.config(text=self.directory)
            self.download_btn["state"] = "normal"


        self.folder_btn = Button(text="select the path", bg=BLUE, font=ACUIRE, fg=LIGHT_YELLOW,
                                 command=folder_btn_clicked, width=15)

        # --------------------------------------------------------------------------------------------------------

        # Music Selector
        # --------------------------------------------------------------------------------------------------------
        def browseFiles():
            filename = filedialog.askopenfilename(initialdir="/",
                                                  title="Select a music",
                                                  filetypes=[("all files", "*.mp3*")])
            self.add_music = filename

        self.button_explore = Button(text="Add Musics", command=browseFiles, font=ACUIRE, bg=BLUE, fg=LIGHT_YELLOW, width=15)

        # Giving position
        self.canvas_avatar.grid(column=0, row=0)
        self.label_name.grid(column=1, row=0)
        self.canvas_logo.grid(column=4, row=0)
        self.folder_btn.grid(column=1, row=1, columnspan=3, pady=10)
        self.label_save.grid(column=1, row=2, columnspan=3, pady=10)
        self.search_entry.grid(column=1, row=3, columnspan=3)
        self.listbox.grid(column=1, row=4, columnspan=3, pady=10)
        self.download_btn.grid(column=1, row=5, columnspan=3, pady=20)
        self.button_explore.grid(column=1, row=6, columnspan=3, pady=20)

        self.window.mainloop()

    def goto_setting(self, event):
        import setting_gui
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
        setting_gui.Setting_GUI(firstname, lastname, email, phone, username, password)

    def download_btn_clicked(self):
        self.download_btn["state"] = "normal"
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.connect((HOST, PORT))
        except:
            print("socket error")
        self.s.send((self.music + "5").encode())
        print("sent")
        PATH = self.label_save.cget("text")
        # try:
        with open(PATH + "\\" + self.music, 'wb') as f:
            print("file has opened")
            buf = self.s.recv(1024*4)
            i = 0
            while buf:
                self.download_btn["state"] = "normal"
                print(buf.__sizeof__())
                f.write(buf)
                i += 1
                print(i)
                buf = self.s.recv(1024*4)
                try:
                    code = buf.decode()
                    print("buf is str")
                    if code == "1":
                        print("code is 1")
                        break
                except UnicodeDecodeError:
                    print(1)

        self.window.update()
        print("end")
        messagebox.showinfo(title="Download was Successful", message=f"{self.music} downloaded in {PATH}")
        # except:
        #     messagebox.showerror(title="ERROR", message="Select a music first")
        #     self.listbox.focus_force()

        self.s.close()


    def destroy(self, event):
        self.s.close()
        print("socket in using page closed")
        pass


# Using_GUI("yazdan", "zandiyevakili", "yazdanzv.1378@gmail.com", "09354416622", "yazdanzv", "yanik1387")
