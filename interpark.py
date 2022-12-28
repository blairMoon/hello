from selenium import webdriver
import os
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

path = os.getcwd() + '/chromedriver'
print(path)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 사이즈조절
driver.get('https://ticket.interpark.com/Gate/TPLogin.asp%27')  # 페이지 이동

driver.switch_to.frame(driver.find_element(
By.XPATH, "//div[@class='leftLoginBox']/iframe[@title='login']"))
userId = driver.find_element(By.ID, 'userId')
userId.send_keys('ID')  # 로그인 할 계정 id
userPwd = driver.find_element(By.ID, 'userPwd')
userPwd.send_keys('PASSWORD')  # 로그인 할 계정의 패스워드
driver.find_element(By.ID, "btn_login").click()
driver.find_element(By.CLASS_NAME, "openid").click()
while(1): pass
