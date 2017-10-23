from selenium import webdriver
from selenium.webdriver.common.keys import Keys



chromepath = r"c:/chrome/chromedriver.exe";

browser = webdriver.Chrome(chromepath);
browser.get("https://google.com");
body = browser.find_element_by_tag_name('body')

body.send_keys(Keys.CONTROL+'t')