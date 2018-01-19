import unittest #import the unittest module
from passlocker import details #importing credentials classs

class TestCredentials(unittest.TestCase):
    '''
    defines test cases for the credential class behaviours

    Args:
        unittest.TestCase: helps in creating test cases
    '''
    def setUp(self):
        '''
        set up method to run before each test cases
        '''
        self.new_account = Credentials("Account","Testname","TestPass")

    def test_init(self):
        '''
        test if the object is initialized properly
        '''
        self.assertEqual(self.new_account.account_name,"Account")
        self.assertEqual(self.new_account.user_name,"Testname")
        self.assertEqual(self.new_account.password,"TestPass")
if __name__ == '__main__':
    unittest.main()
