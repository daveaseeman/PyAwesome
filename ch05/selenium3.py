from selenium import webdriver

from selenium.webdriver.common.keys import Keys


def get_github_link(driver):
    links = driver.find_elements_by_tag_name('a')

    for link in links:
        # Deal with broken links
        if link.get_attribute('href'):
            if "github" in link.get_attribute('href'):
                print("Github link found: ", link.get_attribute('href'))


driver = webdriver.Firefox()

driver.get("http://pythonforengineers.com/articles/")


search_box = driver.find_element_by_name("s")
search_box.send_keys("build reddit bot")
search_box.send_keys(Keys.RETURN)

bot1 = driver.find_element_by_link_text("Build a Reddit Bot Part 1")
bot1.click()

print("Links found on page 1: \n")
get_github_link(driver)

print("\n")


bot2 = driver.find_element_by_partial_link_text("Next")
bot2.click()

print("Links found on page 2: \n")
get_github_link(driver)
print("\n")

bot3 = driver.find_element_by_partial_link_text("Next")
bot3.click()

print("Links found on page 3: \n")
get_github_link(driver)
print("\n")


driver.close()