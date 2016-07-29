from selenium import webdriver
import time

REDDITUSERNAME = ""
REDDITPASS = ""


driver = webdriver.Firefox()

driver.get("https://www.reddit.com/r/python")

username = driver.find_element_by_name("user")
username.send_keys(REDDITUSERNAME)

time.sleep(0.5)
password = driver.find_element_by_name("passwd")
password.send_keys(REDDITPASS)

time.sleep(0.5)
remember_me = driver.find_element_by_name("rem")
remember_me.click()


time.sleep(0.5)
button2 = driver.find_element_by_xpath("//*[contains(text(), 'login')]")
button2.click()

time.sleep(4)

driver.close()





