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
driver.set_window_size(1400, 1000)  # (가로, 세로)
driver.get('https://ticket.interpark.com/Gate/TPLogin.asp') # 페이지 이동
driver.switch_to.frame(driver.find_element(By.XPATH, "//div[@class='leftLoginBox']/iframe[@title='login']"))
userId = driver.find_element(By.ID, 'userId')
userId.send_keys('catherine621') # 로그인 할 계정 id
userPwd = driver.find_element(By.ID, 'userPwd')
userPwd.send_keys('tnqlsl3809!') # 로그인 할 계정의 패스워드
userPwd.send_keys(Keys.ENTER)
driver.get('http://ticket.interpark.com/Ticket/Goods/GoodsInfo.asp?GoodsCode=' + 'goodsCode')
while(1): pass
