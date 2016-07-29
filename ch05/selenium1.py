from selenium import webdriver
import time

driver = webdriver.Firefox()

driver.get("http://pythonforengineers.com/secret/")


text = driver.find_element_by_tag_name("p")

print("Before pressing the button: ", text.text)


## Unreliable and may fail method

button = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[1]/article/div/button")
print(button.text)


## More relieable method
button2 = driver.find_element_by_xpath("//*[contains(text(), 'Super')]")
button2.click()

text = driver.find_element_by_tag_name("p")

print("After pressing the button: ", text.text)

time.sleep(2)

driver.close()