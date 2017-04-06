from .context import Facebook
from .helpers import get_credentials

import unittest


class TestFacebookLogin(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.user, self.password = get_credentials()

    def test_login(self):
        facebook = Facebook(self.user,self.password)
        # TODO Incluir o nome da pessoa no credentials.txt tambem, pra nao ficar fixo aqui.

        # Chrome
        # username = facebook._driver.find_element_by_xpath('//*[@id="u_0_4"]/div[1]/div[1]/div/a/span').text
        username = facebook._driver.find_element_by_xpath("//*[@id='blueBarDOMInspector']/div/div/div/div/div[2]/div/div/div/a/span").text

        # Firefox
        # username = facebook._driver.find_element_by_css_selector('._1k67 > a:nth-child(1) > span:nth-child(2)').text

        self.assertEquals('Alexandre', username)

class TestFacebook(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.user, self.password = get_credentials()
        self.facebook = Facebook(self.user,self.password)


    def test_open_fanpage(self):
        fanpage = self.facebook.open_fanpage('https://www.facebook.com/jdoriajr')

        pagename = fanpage.find_element_by_xpath("//*[@id='pages_navigation']/div/div/div/div/div[3]/a").text
        self.assertEquals('@jdoriajr', pagename)


if __name__ == '__main__':
    unittest.main()
