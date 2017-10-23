
from selenium import webdriver


#                                     Explaination
# in this tutorial we are going to select link with its text as in example 5 , after that will click it     



chromepath = r"c:/chrome/chromedriver.exe";

browser = webdriver.Chrome(chromepath);
browser.get('https://google.co.uk')


about  =   browser.find_element_by_link_text('About')
#now we wait for 5 seconds to make broswer ready to click link
browser.implicitly_wait(5)
 
 #now click the link and the browser will be navigated to about page 
about.click()


browser.close()
