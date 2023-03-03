from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)
x_element = browser.find_element(By.ID, "input_value").text
x = x_element
y = calc(x)

input = browser.find_element(By.ID, "answer")
input.send_keys(y)

button = browser.find_element(By.CSS_SELECTOR, '[type=submit]')
browser.execute_script("return arguments[0].scrollIntoView(true);", button)

first_button = browser.find_element(By.CSS_SELECTOR, '[for=robotCheckbox]').click()
second_radio = browser.find_element(By.CSS_SELECTOR, '[for=robotsRule]').click()

button.click()
time.sleep(5)
