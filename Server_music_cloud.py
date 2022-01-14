import socket
import threading
from _thread import *
import json
import os
import socket

File_PATH = "User_Datas.json"


def fun(c):
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
    c.close()
    print("end")



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
                c.send("0".encode())


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
    i=0
    with open(".\\Music Bank\\" + music_name, 'rb') as f:
        print("Music is sending")
        buf = f.read(30000000)
        c.sendall(buf)
        # while buf:
        #     i += 1
        #     print(i)
        #
        #     buf = f.read(1024 * 4)
        print("music sent successfully")


def send_old_data(c: socket.socket, data: str):
    data = data[0:-1]
    with open(File_PATH, 'r') as f:
        file_data = json.load(f)
    info = file_data[data]
    info_send = json.dumps(info)
    c.send(info_send.encode())


if __name__ == "__main__":

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

