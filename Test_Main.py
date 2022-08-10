import unittest 
from Main import *


class TestMenuWhile(unittest.TestCase):
    def test_While(self):
        #test when user input is not am integer
        self.assertTrue(user_type, 5)
        self.assertFalse(user_type, "a")
        self.assertFalse(user_type, -1)
        self.assertFalse(user_type, 0)
        self.assertTrue(admin_login)
