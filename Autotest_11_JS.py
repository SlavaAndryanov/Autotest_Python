from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.execute_script('document.title="Script executing";')
time.sleep(5)

