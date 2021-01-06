from selenium import webdriver
import time
import math

link = 'http://suninjuly.github.io/get_attribute.html'

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_value = browser.find_element_by_id('treasure').get_attribute('valuex')
    x = x_value
    y = calc(x)

    browser.find_element_by_id('answer').send_keys(y)
    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_id('robotsRule').click()
    browser.find_element_by_class_name('btn').click()

finally:
    time.sleep(5)
    browser.quit()

