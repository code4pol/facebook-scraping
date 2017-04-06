from .context import Facebook
from .helpers import get_credentials
import time

import unittest


class TestFacebookLogin(unittest.TestCase):

    def setUp(self):
        print('TestFacebookLogin.setUp')
        self.user, self.password = get_credentials()

    def test_login(self):
        print('TestFacebook.test_login')
        facebook = Facebook(self.user,self.password)
        # TODO Incluir o nome da pessoa no credentials.txt tambem, pra nao ficar fixo aqui.

        # Chrome
        # username = facebook._driver.find_element_by_xpath('//*[@id="u_0_4"]/div[1]/div[1]/div/a/span').text
        username = facebook._driver.find_element_by_xpath("//*[@id='blueBarDOMInspector']/div/div/div/div/div[2]/div/div/div/a/span").text

        # Firefox
        # username = facebook._driver.find_element_by_css_selector('._1k67 > a:nth-child(1) > span:nth-child(2)').text

        self.assertEquals('Alexandre', username)


class TestFacebook(unittest.TestCase):

    def setUp(self):
        print('TestFacebook.setUp')

        self.user, self.password = get_credentials()
        self.facebook = Facebook(self.user,self.password)

    def tearDown(self):
        print('TestFacebook.tearDown')
        self.facebook.close()

    def test_open_fanpage(self):
        print('TestFacebook.test_open_fanpage')

        fanpage = self.facebook.open_fanpage('https://www.facebook.com/jdoriajr')

        pagename = fanpage.find_element_by_xpath("//*[@id='pages_navigation']/div/div/div/div/div[3]/a").text
        self.assertEquals('@jdoriajr', pagename)

    def test_posts(self):
        print('TestFacebook.test_posts')

        # page_url = 'https://www.facebook.com/jdoriajr'
        page_url = 'https://www.facebook.com/Budegas-Bistr%C3%B4-Na-hora-sai-191059734334020/'

        fanpage = self.facebook.open_fanpage(page_url)

        time.sleep(5)

        # Doria
        # xpath = "//*[@id='mainContainer']/div/div[2]/div[2]/div/div/div/div/div[2]/div/div[3]/div[2]/div/div/div[2]/div/div[3]/div[2]/p"

        # Budega
        xpath = "//*[@id='mainContainer']/div[2]/div[2]/div[2]/div/div/div/div/div[2]/div/div[8]/div[2]/div/div/div/div/div[3]/div[2]/p"

        post = fanpage.find_element_by_xpath(xpath).get_attribute("innerText")

        print('POST=',post)
        self.assertRegex(post, 'Galera, esse candango.*')


if __name__ == '__main__':
    unittest.main()
