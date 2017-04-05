from .context import FacebookLoginPage

import unittest


class TestFacebookLoginPage(unittest.TestCase):
    # .login('alegomes@gmail.com','!2#Pipoc@')

    def test_page_opening (self):
        login_page = FacebookLoginPage()
        self.assertRaises(FileNotFoundError, FacebookLoginPage)

if __name__ == '__main__':
    unittest.main()
