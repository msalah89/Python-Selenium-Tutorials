from selenium import webdriver
import time

#                                     Explaination
# in this tutorial we are going to click about link as  in example 9, after that will get the url form the browser    



chromepath = r"c:/chrome/chromedriver.exe";

browser = webdriver.Chrome(chromepath);
browser.get('https://google.co.uk')


about  =   browser.find_element_by_link_text('About')
#now we wait for 5 seconds to make broswer ready to click link
browser.implicitly_wait(5)
 
 #now click the link and the browser will be navigated to about page 
about.click()

time.sleep(2)
print(browser.current_url)

browser.close()
