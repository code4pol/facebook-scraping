from .context import FacebookLoginPage
from test.support import EnvironmentVarGuard

import unittest


class TestFacebookLoginPage(unittest.TestCase):

    # def setUp(self):
        # self.env = EnvironmentVarGuard()
        # self.env.set('PATH', '../facebook/drivers/:$PATH')

    def test_page_opening (self):
        login_page = FacebookLoginPage()
        self.assertEquals("Facebook - Log In or Sign Up", login_page.get_title())

if __name__ == '__main__':
    unittest.main()
