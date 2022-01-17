import socket
import threading
from _thread import *
import json
import os
import socket
import smtplib

File_PATH = "User_Datas.json"
EMAIL = "musicloudzv@gmail.com"
PASSWORD = "yanik1387"


def fun(c: socket.socket):
    print(type(c))
    data = c.recv(1024)
    info = data.decode()
    print(info)
    try:
        print(info[-1])
    except:
        print("out of range")
    if info[-1] == "1":
        print("sign_up")
        sign_up(c, info)
    elif info[-1] == "3":
        print("checks")
        check(c, info)
    elif info[-1] == "4":
        print("user data changed")
        change_user_data(info)
    elif info[-1] == "5":
        print("music sender")
        music_sender(c, info)
    elif info[-1] == "6":
        print("old infos sent to client")
        send_old_data(c, info)
    elif info[-1] == "7":
        print("code sending...")
        ans = recognize_email_or_username(info)
        if ans == "username":
            print("its username")
            with open(File_PATH, 'r') as f:
                username = info[0:-1]
                file_data = json.load(f)
                print(username)
                email = file_data[username]["email"]
                print(email)
                firstname = file_data[username]["firstname"]
                print(firstname)
                send_email(2, email, firstname, c)
        elif ans == "email":
            print("its an email")
            with open(File_PATH, 'r') as f:
                file_data: dict = json.load(f)
                keys = list(file_data.keys())
                email = info[0:-1]

                for i in keys:
                    if file_data[i]["email"] == email:
                        firstname = file_data[i]["firstname"]
                        print(firstname)
                        print(email)
                        send_email(2, email, firstname, c)


        elif ans == "not found":
            c.send("0".encode())
        else:
            raise Exception("Something went wrong !!!")
    elif info[-1] == "8":
        info = info[0:-1]
        with open(File_PATH, 'r') as f:
            file_data: dict = json.load(f)
            keys = list(file_data.keys())
            if info in keys:
                ans = {"username": info, "password": file_data[info]["password"]}
                c.send(json.dumps(ans).encode())
            else:
                for i in keys:
                    if info == file_data[i]["email"]:
                        username = i
                        password = file_data[username]["password"]
                        ans = {"username": username, "password": password}
                        break
                c.send(json.dumps(ans).encode())
    elif info[-1] == "9":
        ans = recognize_email_or_username(info)
        if ans == "username":
            with open(File_PATH, 'r') as f:
                username = info[0:-1]
                file_data = json.load(f)
                email = file_data[username]["email"]
                firstname = file_data[username]["firstname"]
                send_email(2, email, firstname, c)
        elif ans == "email":
            email = info[0:-1]
            with open(File_PATH, 'r') as f:
                file_data: dict = json.load(f)
                keys = list(file_data.keys())
                for i in keys:
                    if file_data[i]['email'] == email:
                        firstname = file_data[i]["firstname"]
                        send_email(2, email, firstname, c)
        else:
            raise Exception("Something went wrong !!!")

    c.close()
    print("end")


def recognize_email_or_username(data: str):
    data = data[0:-1]
    with open(File_PATH, 'r') as f:
        file_data: dict = json.load(f)
        if data in file_data:
            return "username"
        else:
            print("here i am ")
            keys = list(file_data.keys())
            for i in keys:
                if data == file_data[i]["email"]:
                    print(i)
                    return "email"
            return "not found"


def sign_up(c: socket.socket, data: str):
    flag_email = True
    flag_phone = True
    with open(File_PATH, 'r') as f:
        try:
            file_data = json.load(f)
        except:
            file_data = {}
    data = data[0:-1]
    info = json.loads(data)
    username = list(info.keys())[0]
    email = info[username]['email']
    phone = info[username]['phone']
    firstname = info[username]["firstname"]
    file_keys = list(file_data.keys())

    if username in file_keys:
        print("user exists")
        c.send("1".encode())
    else:
        for i in range(len(file_keys)):
            print(file_data[file_keys[i]]["email"])
            if email == file_data[file_keys[i]]["email"]:
                print("email already exists")
                c.send("2".encode())
                flag_email = False
            if phone == file_data[file_keys[i]]["phone"]:
                print("phone already exists")
                c.send("3".encode())
                flag_phone = False
        if flag_email and flag_phone:
            with open(File_PATH, 'w') as f:
                file_data[username] = info[username]
                json.dump(file_data, f, indent=4)
                send_email(1, email, firstname)
                c.send("0".encode())


def send_email(code, email, firstname, c: socket.socket):
    import random
    global connection
    # Welcome message
    if code == 1:
        connection.sendmail(from_addr=EMAIL, to_addrs=email,
                            msg=f"Subject:Welcome to Music Cloud\n\nDear {firstname}\nWelcome to our app\nWe hope "
                                f"that we can have nice times together")
    elif code == 2:
        security_code = random.randint(10000, 99999)
        connection.sendmail(from_addr=EMAIL, to_addrs=email, msg=f"Subject:Music Cloud - Security Code\n\n"
                                                                 f"Dear {firstname}\n"
                                                                 f"Here is your security code to retrieve your "
                                                                 f"account informations\nCode = {security_code}")
        # sending the security code
        c.send((str(security_code) + "1").encode())
        print("code sent")


def sign_in(c: socket.socket, data: str):
    info = json.loads(data)
    with open(File_PATH, "r") as f:
        try:
            file_data = json.load(f)
        except:
            file_data = ""
        username = info["username"]
        client_datas = file_data[username]
        client_datas = json.dumps(client_datas)
        c.send(client_datas.encode())


def check(c: socket.socket, data: str):
    data = data[0:-1]
    print(data)
    info = json.loads(data)
    print(info)
    username = info["username"]
    password = info["password"]
    with open(File_PATH, 'r') as f:
        try:
            file_data = json.load(f)
            if username in file_data:
                print("checking username")
                if password == file_data[username]["password"]:
                    print("checking password")
                    print("sign_in")
                    sign_in(c, data)
                else:
                    print("password is wrong")
                    c.send("2".encode())
            else:
                c.send("3".encode())
        except:
            file_data = ""
            # didn't signed up
            c.send("3".encode())


def change_user_data(data: str):
    data = data[0:-1]
    info: dict = json.loads(data)
    username = list(info.keys())[0]
    with open(File_PATH, 'r') as f:
        file_data: dict = json.load(f)
    file_data[username] = info[username]
    with open(File_PATH, 'w') as f:
        json.dump(file_data, f, indent=4)


def music_sender(c: socket.socket, data: str):
    music_name = data[0:-1]
    i = 0
    with open(".\\Music Bank\\" + music_name, 'rb') as f:
        print("Music is sending")
        buf = f.read(1024 * 4)
        while buf:
            i += 1
            print(i)
            c.send(buf)
            buf = f.read(1024 * 4)
        c.shutdown(socket.SHUT_RDWR)
        print("music sent successfully")


def send_old_data(c: socket.socket, data: str):
    data = data[0:-1]
    with open(File_PATH, 'r') as f:
        file_data = json.load(f)
    info = file_data[data]
    info_send = json.dumps(info)
    c.send(info_send.encode())


if __name__ == "__main__":
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=EMAIL, password=PASSWORD)

    host = ""
    port = 80

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("binded")

    s.listen(10)
    print("listening")

    # files = list(os.walk('.'))[0][2]
    # if "User_datas.json" not in files:
    #     with open("User_Datas.json", "w") as f:
    #         pass

    while True:
        c, addr = s.accept()
        print('Connected to :', addr[0], ':', addr[1])
        # print_lock.acquire()
        start_new_thread(fun, (c,))
