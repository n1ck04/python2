import re

def validate():
    # password = input("Enter a password: ")
    while True:
        password = input("Enter a password: ")
        if len(password)>12 or len(password)<8:
            print("Make sure your password have 8 to 12 letters")
        elif re.search('[0-9]',password) is None:
            print("Make sure your password has a number in it")
        elif re.search('[A-Z]',password) is None:
            print("Make sure your password has a capital letter in it")
        elif re.search('[@,#,&,%,!,$,*,(,),+,=,/,?,^]',password) is None:
            print("Make sure your password has a special character in it")
        else:
            print("Your password seems fine\nPassword has been saved into password manager")
            with open('passwords.txt', 'a') as file:
                file.write(password+',\n')
            break

validate()

with open('passwords.txt', 'r') as file:
    f = file.read()
    print('===*+++---BELOW ARE YOUR OLD SAVED PASSWORDS---+++*===')
    #file.write('')
    print(f)

    # a=input("enter the saved password to open")
    # if  a == validate().password:
    #     for i in f:
    #         print(i)
    # else:
    #     print("password is wrong")
    #