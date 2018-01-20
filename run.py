#!/usr/bin/env python3.6
import passlocker
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
    print('''    Do you ever want to easily access your passwords
    without having to memorize??
    Well here is a chance to save all your passwords in a
    single location''')

if __name__ == '__main__':
    main()
