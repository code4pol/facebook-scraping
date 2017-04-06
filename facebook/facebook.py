from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# from selenium.webdriver.common.keys import Keys

# class Facebook:
#
#     instance = None
#
#     def __init__(self, username, password):
#         print('Facebook.__init__')
#         if not Facebook.instance:
#             Facebook.instance = Facebook.__FacebookLoginPage(username, password)
#
#     # Delegator
#     def __getattr__(self, name):
#         return getattr(self.instance, name)
#
#     def __del__(self):
#         # self.instance._driver.close()
#         self.instance._driver.quit()
#         print('FacebookLoginPage destroyed')
#
#     # Singleton
#     # http://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html
#     class __FacebookLoginPage:
#
#         _login_url = "https://www.facebook.com/"
#         logged = False
#
#         def __init__(self, username, password):
#             print('__FacebookLoginPage.__init__')
#             self._driver = webdriver.Chrome('/Users/alegomes/code/facebook-scraping/drivers/chromedriver')
#             # self._driver = webdriver.Firefox(executable_path='/Users/alegomes/code/facebook-scraping/drivers/geckodriver')
#             self._driver.get(self._login_url)
#             assert "Facebook - Log In or Sign Up" in self._driver.title
#             self._email_field = self._driver.find_element_by_id('email')
#             self._pass_field = self._driver.find_element_by_id('pass')
#             self._login_button = self._driver.find_element_by_id('u_0_p')
#
#             self._login(username,password)
#
#         def __del__(self):
#             # self._driver.close()
#             self._driver.quit()
#             print('__FacebookLoginPage destroyed')
#
#         def _login(self, user, password):
#             if not self.logged:
#                 self._email_field.send_keys(user)
#                 self._pass_field.send_keys(password)
#                 # self._login_button.click()
#                 self._pass_field.submit()
#                 self.logged = True
#
#
#         def open_fanpage(self, url):
#             self._driver.get(url)
#             return self._driver
#
#         def close(self):
#             self._driver.quit()



class Facebook:

    _login_url = "https://www.facebook.com/"
    logged = False

    def __init__(self, username, password):
        print('Facebook.__init__')
        self._driver = webdriver.Chrome('/Users/alegomes/code/facebook-scraping/drivers/chromedriver')
        # self._driver.wait = WebDriverWait(self._driver, 5)

        # self._driver = webdriver.Firefox(executable_path='/Users/alegomes/code/facebook-scraping/drivers/geckodriver')
        self._driver.get(self._login_url)
        assert "Facebook - Log In or Sign Up" in self._driver.title
        self._email_field = self._driver.find_element_by_id('email')
        self._pass_field = self._driver.find_element_by_id('pass')
        self._login_button = self._driver.find_element_by_id('u_0_p')

        self._login(username,password)

    def __del__(self):
        # self._driver.close()
        self._driver.quit()
        print('Facebook destroyed')

    def _login(self, user, password):
        print('Facebook login')
        if not self.logged:
            self._email_field.send_keys(user)
            self._pass_field.send_keys(password)
            # self._login_button.click()
            self._pass_field.submit()
            self.logged = True


    def open_fanpage(self, url):
        print('Facebook open_fanpage')
        self._driver.get(url)

        # try:
        #     box = self._driver.wait.until(EC.presence_of_element_located(
        #         (By.XPATH, "//*[@id='mainContainer']/div/div[2]/div[2]/div/div/div/div/div[2]/div/div[3]/div[2]/div/div/div[2]/div/div[3]/div[2]/p")))
        #     # button = self._driver.wait.until(EC.element_to_be_clickable(
        #     #     (By.NAME, "btnK")))
        #     # box.send_keys(query)
        #     # button.click()
        # except TimeoutException:
        #     print("Nenhum post encontrado na página")

        # print('Iniciando contagem...')
        # self._driver.implicitly_wait(5)
        # print('Fim da contagem.')
        return self._driver

    def close(self):
        print('Facebook close')
        self._driver.quit()



# import requests

# from lxml import etree
# from lxml.cssselect import CSSSelector
# from io import StringIO
# import re

# login_url = "https://www.facebook.com/"
# page_url = "https://www.facebook.com/jdoriajr/"

# r = requests.get(url)
# html = r.text
# if html:
# 	parser = etree.HTMLParser()
# 	tree   = etree.parse(StringIO(html), parser)
# 	# print(r.text)
# 	# print(tree.xpath('//*[@id="content"]/div[2]/div/section/table/tbody/tr[3]/td/p/img'))
# 	sel = CSSSelector('.report-chart')
# 	# print(tree.xpath("/html/body/div[@id='page']/section[@id='content']//table"))
# 	print('css=',tree.xpath(sel.path))
# 	print('xpath=',tree.xpath("//table"))


# urllib.request.urlretrieve(url, "local-filename.jpg")
#
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
# driver = webdriver.Chrome('./drivers/chromedriver')
# driver.get(login_url)
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()