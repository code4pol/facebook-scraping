from .context import FacebookLoginPage

import unittest


class TestFacebookLoginPage(unittest.TestCase):

    def test_page_opening (self):
        login_page = FacebookLoginPage()
        self.assertEquals("Facebook - Login or Sign Up", login_page.get_title())

if __name__ == '__main__':
    unittest.main()
