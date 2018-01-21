#!/usr/bin/env python3.6
import random
import passlocker
#methods for user
def create_user(name,pwd):
    '''
    function to create new user
    '''
    new_user = user(name,pwd)
    return new_user
def save_user(user):
    '''
    function to save user details
    '''
    user.save_user()
def generate_password(user):
    '''
    function to generate password
    '''
    user.generate_password()

#methods for credentials
def create_account(account_name, user_name, password):
    '''
    function to create new account
    '''
    new_account = credentials(account_name, user_name, password)
    return new_account

def save_account(account):
    '''
    function to save account
    '''
    account.save_account()

def del_account(account):
    '''
    function to delete account
    '''
    account.delete_account()

def find_account(account_name):
    '''
    function to find account by account name
    '''
    return credentials.find_by_account(account_name)

def check_existing_account(account_name):
    '''
    function that checks if account exists
    '''
    return credentials.account_exists(account_name)

def display_accounts():
    '''
    function that returns saved accounts
    '''
    return credentials.display_accounts()


def main():
    print("--------------------Password Locker-------------------")
    print('''Do you ever want to easily access your passwords
without having to memorize??
        Well here is a chance to save all your passwords in a
        single location''')
    print("\n")
    print("Enter your name here: ")
    username = input()
    print("*"*78)
    print(f"Hello {username}.\nDo you want to enter a password or we automatically generate for you?")
    print('''
        Press:
                    g- generate new password
                    c- create your own password
          ''')
    pwd_click = input()
    if (pwd_click  == 'g'):
        chars = '1234567890abcdefghijklmnop?/@-' #characters to choose from
        length = int(input("Enter the length of password you want: "))
        pwdinput = ''
        for c in range(length):
            pwdinput += random.choice(chars) #generate random password
        print (pwdinput)
        print(f"{username} your password is {pwdinput}")

    else:
        print("enter your password: ")
        pwdinput = input()
        print(f"{username} your password is {pwdinput}")

        print("\n"*2)

    print("To continue reenter your details")
    print("*"*78)
    print("Enter your username again: ")
    name = input()
    print("Enter your password: ")
    pwd = input()
    if (name == username and pwd == pwdinput):
        print('\n')
        

    else:
        print('''Incorrect Name or Password
Run the application again''')

if __name__ == '__main__':
    main()
