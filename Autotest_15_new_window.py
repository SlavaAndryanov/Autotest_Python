from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    first_button = browser.find_element(By.TAG_NAME, 'button')
    first_button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element(By.ID, 'input_value').text
    y = calc(x)

    input_x = browser.find_element(By.ID, 'answer')
    input_x.send_keys(y)

    final_button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    final_button.click()

finally:
    time.sleep(3)
    quit()