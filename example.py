from facebook.facebook import Facebook

credentials_file = open('credentials.txt')
credentials = credentials_file.readline()
username, password  = credentials.split(':')

facebook = Facebook(username,password)
# page = facebook.open_fanpage('https://www.facebook.com/Budegas-Bistr%C3%B4-Na-hora-sai-191059734334020/')
page = facebook.open_fanpage('https://www.facebook.com/jdoriajr/')

# xpath = "//*[@id='mainContainer']/div[2]/div[2]/div[2]/div/div/div/div/div[2]/div/div[8]/div[2]/div/div/div/div/div[3]/div[2]/p"
xpath = '//*[@id="js_3"]'
post = page.find_element_by_xpath(xpath).get_attribute("innerText")
print('POST=', post)

page.quit()
