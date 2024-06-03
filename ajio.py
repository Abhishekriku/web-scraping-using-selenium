from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
#creating service object for the chrome webdriver
s = Service("C:/Users/HP/Desktop/chromedriver.exe")
#creating driver object to drive google chrome from pycharm
driver = webdriver.Chrome(service = s)

#to get to a webpage
driver.get("https://www.ajio.com/men-backpacks/c/830201001")

#to find the height of the page
old_height = driver.execute_script('return document.body.scrollHeight')

counter = 1
#to scroll to the bottom of the page
while True:

    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(2)
    new_height = driver.execute_script('return document.body.scrollHeight')

    print(counter)
    counter += 1
    print(old_height)
    print(new_height)

    if new_height==old_height:
        break
    old_height = new_height


html = driver.page_source

with open('ajio.html','w',encoding= 'utf-8') as f:
    f.write(html)

time.sleep(500)