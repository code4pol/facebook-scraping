from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

class FacebookLoginPage:

    _login_url = "https://www.facebook.com/"
    _page_url = "https://www.facebook.com/jdoriajr/"

    def __init__(self):
        self._driver = webdriver.Chrome('/Users/alegomes/code/facebook-scraping/drivers/chromedriver')
        # self._driver = webdriver.Firefox()
        self._driver.get(self._login_url)
        assert "Facebook - Log In or Sign Up" in self._driver.title
        email_field = self._driver.find_element_by_id('email')
        pass_field = self._driver.find_element_by_id('pass')

    def __del__(self):
        self._driver.quit()

    def get_title(self):
        # return "Facebook - Login or Sign Up"
        return self._driver.title

    def get_login_field(self):
        return None

class FacebookFanPage:

    def __init__(self):
        pass


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