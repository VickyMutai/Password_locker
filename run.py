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
