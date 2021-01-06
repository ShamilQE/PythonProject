from selenium import webdriver
import time

link = 'http://suninjuly.github.io/math.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    #Radio button checked by default
    # people_radio = browser.find_element_by_id('peopleRule')
    # people_checked = people_radio.get_attribute('checked')
    # print("Value of radio people: ",people_checked)
    # assert people_checked is not None, "People of radio is not selected by default"
    # assert people_checked == "true", "People of radio is not selected by default"


    #Radio button is not checked by default
    robots_rule = browser.find_element_by_id('robotsRule')
    robots_checked = robots_rule.get_attribute('checked')
    print('Value of radio Robots: ',robots_checked)
    # assert robots_checked == 'true', "Robots radio button is not checked by default"
    assert robots_checked is None

finally:
    time.sleep(1)
    browser.quit()
