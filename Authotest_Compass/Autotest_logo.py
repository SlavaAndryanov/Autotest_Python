from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "https://compass-dev-version.webflow.io/#hero"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, '#w-dropdown-toggle-6>[class=cta__dd-text]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    time.sleep(1)

    logo = browser.find_element(By.CLASS_NAME, 'logo__image')
    logo.click()
    time.sleep(3)

finally:
    browser.quit()
