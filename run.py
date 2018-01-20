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
