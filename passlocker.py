class credentials:
    '''
    class that generates new instances of credentials
    '''
    credential_list = []
    def __init__(self,account_name,user_name,password):
        '''
        init method helps us define properties for our objects
        '''
        self.account_name = account_name
        self.user_name = user_name
        self.password = password

    def save_account(self):
        '''
        save contact object into credential_list
        '''
        credentials.credential_list.append(self)

    def delete_account(self):
        '''
        delete account
        '''
        credentials.credential_list.remove(self)

    @classmethod
    def find_by_account(cls,account_name):
        '''
        search for account, returns a list containing the account credentials
        args:
             account_name: that will be used to search
        Returns:
            account credentials
        '''
        for account in cls.credential_list:
            if contact.user_name == user_name:
                return account
