from selenium import webdriver


chromepath = r"c:/chrome/chromedriver.exe";

driver = webdriver.Chrome(chromepath);
driver.get("https://google.com");
assert('Google' in driver.title);