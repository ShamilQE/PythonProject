from selenium import webdriver
import time
import math

link = 'http://suninjuly.github.io/math.html'

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    browser.find_element_by_id('answer').send_keys(y)

    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()
    radio_btn = browser.find_element_by_id("robotsRule")
    radio_btn.click()
    submit = browser.find_element_by_tag_name('button.btn')
    submit.click()

finally:
    time.sleep(5)
    browser.quit()

