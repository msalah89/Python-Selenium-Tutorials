

from selenium import webdriver


#                                     Explaination
# in this tutorial we are going to select link by xpath     



chromepath = r"c:/chrome/chromedriver.exe";

browser = webdriver.Chrome(chromepath);
browser.get('https://www.google.com/')

try:
    browser.find_element_by_xpath("//a[@class='_Gs']")
    print('Test Pass :Partial Link Text Found ')
except Exception as e:
    print ('Exception Found ', format(e))
    
browser.close()
