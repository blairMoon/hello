from selenium import webdriver
import os

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
path = os.getcwd() + '/chromedriver'
print(path)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://naver.com')


driver.find_element(By.ID, 'query').click()
driver.find_element(By.ID, 'query').send_keys("증권")
driver.find_element(By.ID, 'search_btn').click()
csp = driver.find_element(By.CLASS_NAME,'csp').text
csd = driver.find_element(By.CLASS_NAME,'csd').text
print(csp)
print(csd)

while(1): pass
