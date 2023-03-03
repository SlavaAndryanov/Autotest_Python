from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)

    input_firstName = browser.find_element(By.NAME, 'firstname')
    input_firstName.send_keys('Some name')

    input_lastName = browser.find_element(By.NAME, 'lastname')
    input_lastName.send_keys('Some last name')

    input_Email = browser.find_element(By.NAME, 'email')
    input_Email.send_keys('Some@Email')

    file_button = browser.find_element(By.ID, 'file')
    with open('test1.txt', 'w') as file:
        file.write('test1 for mls 228')
    path = os.getcwd() + '/' + file.name
    file_button.send_keys(path)

    button = browser.find_element(By.CSS_SELECTOR, '[type=submit]')
    button.click()

finally:
    time.sleep(5)
    browser.quit()