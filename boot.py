import time
import os

print("""
███╗░░░███╗░█████╗░███████╗         ░█████╗░░██████╗
████╗░████║██╔══██╗╚════██║         ██╔══██╗██╔════╝
██╔████╔██║███████║░░███╔═╝         ██║░░██║╚█████╗░
██║╚██╔╝██║██╔══██║██╔══╝░░         ██║░░██║░╚═══██╗
██║░╚═╝░██║██║░░██║███████╗         ╚█████╔╝██████╔╝
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚══════╝         ░╚════╝░╚═════╝░
""")

print("""
[1] Continue with setup
[2] Ive already done setup
""")

setup = input("[?]: ")
if setup == '1':
    name = input(str("Please enter your username to be displayed: "))
    pas = input(str("Please enter your password: "))

    with open('user/username.txt', 'w') as f:
        f.writelines(name)

    lines2 = [pas]
    with open('user/password.txt', 'w') as f:
        f.writelines(pas)
    print("Setup complete!")
    input("Press enter to close window: ")

if setup == '2':
    login_pass = open('user/password.txt')
    login_name = open('user/username.txt')
    l_p = login_pass.read()
    l_n = login_name.read()

while True:
    login = input(str("Please enter the password to " + l_n + ": "))
    if login == l_p:
        os.startfile('MAZOSMAIN.py')

        break
    else:
        print("Wrong password")
