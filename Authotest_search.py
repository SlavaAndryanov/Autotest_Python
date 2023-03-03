from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = 'https://www.yandex.ru/chrome/newtab'
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(link)

search_string = browser.find_element(By.CSS_SELECTOR, 'input[class*=input__control]')
search_string.send_keys('Skyeng')
button = browser.find_element(By.CSS_SELECTOR, 'button[class*=mini-suggest__button]')
button.click()
testing = WebDriverWait(browser, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class*=serp-title_type_supertitle]'))).text
print(testing)

is_True = 'Skyeng'
assert testing == is_True, f'Тест не пройден, текущее значение {testing}'
browser.quit()