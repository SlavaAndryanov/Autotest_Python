from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_number = browser.find_element(By.ID, 'num1').text
    second_number = browser.find_element(By.ID, 'num2').text
    sum_number = int(first_number) + int(second_number)
    sum_number = str(sum_number)

    select = Select(browser.find_element(By.ID, 'dropdown'))
    select.select_by_value(sum_number)

    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()
finally:
    time.sleep(10)
    browser.quit()