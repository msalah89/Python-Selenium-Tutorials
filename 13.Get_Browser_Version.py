from selenium import webdriver

#                      Explaination
# here we are going to , get chrome browser version  


chromepath = r"c:/chrome/chromedriver.exe";

browser = webdriver.Chrome(chromepath);
browser.get("https://google.com");

print (browser.capabilities['version'])

browser.close()