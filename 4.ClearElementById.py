import time 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# in this tutorial I will show you how to get element by id , write on it and clear it 



chromepath = r"c:/chrome/chromedriver.exe";

browser = webdriver.Chrome(chromepath);
browser.get("https://google.com");

# Get Element by Id

search = browser.find_element_by_id('lst-ib')
search.send_keys('Python 3 ')
search.send_keys(Keys.SPACE)

#Now I will Clear the text after 2 seconds
time.sleep(2)
 
search.clear()

#Now I will Search for selenium tutorial
search.send_keys("Selenium Python Tutorial ")
search.send_keys(Keys.ENTER)