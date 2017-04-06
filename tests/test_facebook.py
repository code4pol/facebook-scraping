from .context import Facebook, FacebookFanPage
from .helpers import get_credentials

import unittest


class TestFacebook(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.user, self.password = get_credentials()

    def test_login(self):
        facebook = Facebook()
        self.login = facebook.login(self.user,self.password)
        # TODO Incluir o nome da pessoa no credentials.txt tambem, pra nao ficar fixo aqui.

        # Chrome
        username = facebook._driver.find_element_by_xpath('//*[@id="u_0_4"]/div[1]/div[1]/div/a/span').text

        # Firefox
        # username = facebook._driver.find_element_by_css_selector('._1k67 > a:nth-child(1) > span:nth-child(2)').text

        self.assertEquals('Alexandre', username)


    # def test_multiple_login(self):
    #     login_page = FacebookLoginPage()
    #     self.login = login_page.login(self.user, self.password)
    #     self.assertEquals('Alexandre', login_page._driver.find_element_by_xpath('//*[@id="u_0_4"]/div[1]/div[1]/div/a/span').text)

    # def test_open_fanpage(self):
    #     # login_page = facebook()
    #     if not login_page.logged:
    #         login = login_page.login(self.user, self.password)
    #
    #     fanpage = FacebookFanPage(login,'https://www.facebook.com/jdoriajr')
    #     self.assertEquals('@jdoriajr', self.login.find_element_by_xpath('//*[@id="js_kss"]').text)

if __name__ == '__main__':
    unittest.main()
