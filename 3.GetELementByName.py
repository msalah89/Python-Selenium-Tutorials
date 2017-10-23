import time 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#                                       Explaination
#in this example we are going to use find_element_by_name method to select google search input which has name
#Google input's name is "q" we write our search term and press keyboard key  enter 

chromepath = r"c:\chrome/chromedriver.exe";
driver = webdriver.Chrome(chromepath)
driver.get("https://www.google.com")
q = driver.find_element_by_name("q")
q.send_keys("what is time now ?")

q.send_keys(Keys.RETURN)