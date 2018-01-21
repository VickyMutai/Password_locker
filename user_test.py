import unittest #import the unittest module
from passlocker import user

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
        self.new_user = user("pwd")

    def test_init(self):
        '''
        test if object is initializd correctly
        '''
        self.assertEqual(self.new_user.pwd,"pwd")

if __name__ == '__main__':
    unittest.main()
