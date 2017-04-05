from .context import FacebookLoginPage
from test.support import EnvironmentVarGuard

import unittest


class TestFacebookLoginPage(unittest.TestCase):

    def setUp(self):
        self._login_page = FacebookLoginPage()

    def test_title (self):
        self.assertEquals("Facebook - Log In or Sign Up", self._login_page.get_title())

if __name__ == '__main__':
    unittest.main()
