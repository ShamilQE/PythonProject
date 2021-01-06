from selenium import webdriver
import time

# link = 'http://suninjuly.github.io/registration1.html'
link = 'http://suninjuly.github.io/registration2.html'

""" Scenario when only mandatory fields completed and could register successfully"""

try:
    browser = webdriver.Chrome()
    browser.get(link)
    # m_fields = browser.find_elements_by_tag_name('input[type="text"]')
    # for field in m_fields:
    #     field.send_keys("Shamil", "Afandiyev", "fake@gmail.com",)

    first_name = browser.find_element_by_class_name("first")
    first_name.send_keys("Shamil")
    second_name = browser.find_element_by_tag_name('input[placeholder="Input your last name"]')
    second_name.send_keys("Afandiyev")
    third_name = browser.find_element_by_class_name("third")
    third_name.send_keys("fake@gmail.com")
    submit = browser.find_element_by_css_selector("button.btn")
    submit.click()

    time.sleep(1)

    welcome_text_elmt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elmt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(5)
    browser.quit()

