import re

while True:
    def conNum(string):
        return any(i.isdigit() for i in string)
    userPassword = input("Enter password>")
    passwordPoints = 0
    length = len(userPassword)
    status = 0

    if length < 1:
        print("Password strength: non-existent")
    elif length >= 18:
        status = status + 2
    
    status = status + 1
    if length <= 7:
        status = status - 1
    elif length >= 13:
        status = status + 1
    if userPassword.islower() & conNum(userPassword):
        status = status
    elif userPassword.isupper() & conNum(userPassword):
        status = status
    elif userPassword.islower() or userPassword.isupper() or userPassword.isdigit():
        status = status - 1
    if status <= 0:
        print("Password strength: Weak")
        #break
    elif status == 1:
        print("Password strength: Medium")
        #break
    elif status >= 2:
        print("Password strength: Strong")
        #break
    