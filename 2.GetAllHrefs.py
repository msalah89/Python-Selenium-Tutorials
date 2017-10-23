#this is implementation of python selenium tutorial video series 



from selenium  import webdriver
import time 


chromepath = r"c:/chrome/chromedriver.exe";

driver = webdriver.Chrome(chromepath);

driver.get('http://onecore.net');
ids= driver.find_elements_by_xpath('//*[@href]');


for ii in ids:
    print (ii.get_attribute('href'))
    time.sleep(1)
driver.close()