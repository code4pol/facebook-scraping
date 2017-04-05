from .context import FacebookLoginPage
from test.support import EnvironmentVarGuard

import unittest


class TestFacebookLoginPage(unittest.TestCase):

    def setUp(self):
        # Crie um arquivo chamado credentials.txt na raiz do projeto
        # contendo, na primeira linha, seu usuario e senha do facebook
        # separados por :
        # Exemplo:
        # joao@gmail.com:n1ngu3msab3minhasenh4
        #
        credentials_file = open('../credentials.txt')
        credentials = credentials_file.readline()
        self.user, self.password = credentials.split(':')


    def test_login(self):
        login_page = FacebookLoginPage()
        # Se a pagina nao abrir corretamente, sera lancada a excecao NoSuchElementException
        self.assertTrue(True)

    def test_login(self):
        login_page = FacebookLoginPage()
        login_page.login(self.user,self.password)
        self.assertEquals('Alexandre',login_page._driver.find_element_by_xpath('//*[@id="u_0_4"]/div[1]/div[1]/div/a/span').text)

if __name__ == '__main__':
    unittest.main()
