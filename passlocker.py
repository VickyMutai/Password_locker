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
