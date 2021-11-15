from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random


driver = webdriver.Chrome('C:/Users/Moisés/Desktop/chromedriver')
driver.get("https://www.reddit.com/")
driver.maximize_window()
time.sleep(2)
driver.execute_script("window.scrollTo(0, 300)") 
time.sleep(4)
driver.execute_script("window.scrollTo(300, 600)") 
time.sleep(4)
driver.execute_script("window.scrollTo(600, 900)") 
time.sleep(4)
driver.execute_script("window.scrollTo(900, 1200)") 
time.sleep(4)
driver.execute_script("window.scrollTo(1200, 1500)") 
time.sleep(4)
driver.execute_script("window.scrollTo(1500, 1800)") 
time.sleep(4)
driver.execute_script("window.scrollTo(1800, 2100)") 
time.sleep(4)
driver.execute_script("window.scrollTo(2100, 2400)") 



time.sleep(4)
driver.close()