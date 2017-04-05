from .context import FacebookLoginPage
from test.support import EnvironmentVarGuard

import unittest


class TestFacebookLoginPage(unittest.TestCase):

    # def setUp(self):
    #     self._login_page = FacebookLoginPage()

    def test_login(self):
        login_page = FacebookLoginPage()
        # Se a pagina nao abrir corretamente, sera lancada a excecao NoSuchElementException
        self.assertTrue(True)

    # def test_title (self):
    #     self.assertEquals("Facebook - Log In or Sign Up", self._login_page.get_title())

    # def test_login_fields(self):
    #     self.assertEquals(1,len(self._login_page.get_login_field()))

if __name__ == '__main__':
    unittest.main()
