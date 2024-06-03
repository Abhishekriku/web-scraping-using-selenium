from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

s = Service("C:/Users/HP/Desktop/chromedriver.exe")

driver = webdriver.Chrome(service=s)

driver.get("https://www.smartprix.com/mobiles")
time.sleep(2)

driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]/input').click()

time.sleep(2)

driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[2]/input').click()

time.sleep(10)

