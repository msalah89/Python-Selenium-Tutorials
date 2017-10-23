from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


#                                     Explaination
# in this tutorial we are going to Refresh webpage , we will use 2 methods first : refresh method , second , we will use keyboard shortcut f5     



chromepath = r"c:/chrome/chromedriver.exe";

browser = webdriver.Chrome(chromepath);
browser.get('https://www.wikipedia.org')


# first method refresh

time.sleep(2)
browser.refresh()


#second method : keyboard shortcut f5
time.sleep(2)
browser.find_element_by_tag_name('body').send_keys(Keys.F5)


#end
time.sleep(2)
browser.close()
