import time
import os
import socket
import psutil

battery = psutil.sensors_battery()
login_pass = open('user/password.txt')
login_name = open('user/username.txt')
l_p = login_pass.read()
l_n = login_name.read()
print("""
███╗░░░███╗░█████╗░███████╗         ░█████╗░░██████╗
████╗░████║██╔══██╗╚════██║         ██╔══██╗██╔════╝
██╔████╔██║███████║░░███╔═╝         ██║░░██║╚█████╗░
██║╚██╔╝██║██╔══██║██╔══╝░░         ██║░░██║░╚═══██╗
██║░╚═╝░██║██║░░██║███████╗         ╚█████╔╝██████╔╝
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚══════╝         ░╚════╝░╚═════╝░
""")
print("WELCOME " + l_n)
print("The date is: " + time.strftime("%m/%d/%y"))

print("""
[1] To Open Text Editor
[2] To Open File Explorer
[3] To Configure and Open BIOS
[4] To Close OS Safely
""")
select = input("[?]: ")

if select == '1':
    os.startfile('edit.py')

if select == '2':
    os.startfile('file.py')
    # print("""
    # ██████████████████████████████████████████████████████████████████████████████████████████████████████
    # ███████████████████████████████████████MAZ OS FILE EXPLORER ██████████████████████████████████████████
    # ██████████████████████████████████████████████████████████████████████████████████████████████████████
    # ██  File name: █                                                                                    ██
    # ██████████████████████████████████████████████████████████████████████████████████████████████████████
    # ██                                                                                                  ██
    # ██                                                                                                  ██
    # ██                                                                                                  ██
    # ██                                                                                                  ██
    # ██                                                                                                  ██
    # ██                                                                                                  ██
    # ██                                                                                                  ██
    # ██                                                                                                  ██
    # ██                                                                                                  ██
    # ██                                                                                                  ██
    # ██                                                                                                  ██
    # ██                                                                                                  ██
    # ██                                                                                                  ██
    # ██                                                                                                  ██
    # ██                                                                                                  ██
    # ██                                                                                                  ██
    # ██                                                                                                  ██
    # ██████████████████████████████████████████████████████████████████████████████████████████████████████

#    """)

if select == '3':
    while True:
        b_login = input(str("Please enter the password to " + l_n + ": "))
        if b_login == l_p:
            print("Opening BIOS")
            host_name = socket.gethostname()
            host_ip = socket.gethostbyname(host_name)
            print("[1] USER NAME: " + l_n)
            print("[1] PASSWORD: " + l_p)
            print("HOST NAME: ", host_name)
            print("LOCAL IP: " + host_ip)

            print("""
            [1] Change Username
            [2] Change Password
            """)

            edit_b = input("Enter [?] to change setting: ")
            if edit_b == '1':
                edit_n = input("Enter new username: ")
                with open('user/username.txt', 'w') as f:
                    f.writelines(edit_n)
                print("Username changed to " + edit_n)
                input("Press enter to close window")

            if edit_b == '2':
                edit_p = input("Enter new password: ")
                with open('user/password.txt', 'w') as f:
                    f.writelines(edit_n)
                print("Password changed to " + edit_p)
                input("Press enter to close window")
    else:
        print("Wrong password to " + l_n)
