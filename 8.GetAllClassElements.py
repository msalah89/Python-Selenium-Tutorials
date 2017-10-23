

from selenium import webdriver


#                                     Explaination
# in this tutorial we are going enumerate all classed of elements in the page , we will not mention class name 
#we will use method find_elements_by_xpath to get elements array



chromepath = r"c:/chrome/chromedriver.exe";

browser = webdriver.Chrome(chromepath);
browser.get('https://www.google.com/')

 
id =   browser.find_elements_by_xpath("//*[@class]")
       
for ii in id:
    print(ii.get_attribute('class'))

browser.close()
