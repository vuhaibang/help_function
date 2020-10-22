from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = "https://brightside.me/"
driver = webdriver.Firefox()
driver.get(url)
body = driver.find_element_by_css_selector('body')
for e in driver.find_elements_by_xpath("//a[@href]"):
    href = e.get_attribute('href')