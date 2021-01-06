
from selenium import webdriver
import time

link = 'http://suninjuly.github.io/find_xpath_form'



try:

    browser = webdriver.Chrome()

    browser.implicitly_wait(10)

    browser.get(link)
    input = browser.find_element_by_name("first_name")
    input.send_keys("Shamil")
    input1 = browser.find_element_by_name("last_name")
    input1.send_keys("Afandiyev")
    input2 = browser.find_element_by_class_name("city")
    input2.send_keys("SLC")
    input3 = browser.find_element_by_id("country")
    input3.send_keys("USA")
    submit = browser.find_element_by_xpath('/html/body/div/form/div[6]/button[3]')
    submit.click()

finally:

    # time.sleep(10)
    browser.quit()


