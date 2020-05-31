from time import sleep
from selenium import webdriver

browser = webdriver.Firefox()
brower.implicitly_wait(5)

browser.get('https://www.instagram.com/')

login_link = browser.find_element_by_xpath("//a[text()='Log in']")
login_link.click()

sleep(2)

username_input = browser.find_element_by_css_selector("input[name='username']")
username_input = browser.find_element_by_css_selector("input[name='password']")

sleep(5)

browser.close()