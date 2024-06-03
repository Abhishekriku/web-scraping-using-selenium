# open google.com
# search campusx
# learnwith.campusx.in
# dsmp course page             AUTOMATION
import selenium

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
#making an object to connect to the google chrome driver
s = Service("C:/Users/HP/Desktop/chromedriver.exe")

driver = webdriver.Chrome(service = s)
driver.get(('http://www.google.com'))
time.sleep(2)

#fetch the search input box using xpath
user_input = driver.find_element(by= By.XPATH, value='//*[@id="APjFqb"]')
user_input.send_keys('campusx')
user_input.send_keys(Keys.ENTER)

time.sleep(2)

link = driver.find_element(by=By.XPATH, value = '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a')
link.click()

time.sleep(2)

link2 = driver.find_element(by=By.XPATH, value = '/html/body/div[1]/header/section[2]/a[8]')
link2.click()

time.sleep(10)