from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    input_1 = browser.find_element(By.ID, 'answer')
    input_1.send_keys(y)

    check_element = browser.find_element(By.ID, 'robotCheckbox')
    check_element.click()

    radio_element = browser.find_element(By.ID, 'robotsRule')
    radio_element.click()

    button_element = browser.find_element(By.CLASS_NAME, 'btn-default')
    button_element.click()
    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()


