from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random


driver = webdriver.Chrome('C:/Users/Moisés/Desktop/chromedriver')

word_list=["ballons",    "raspberry pie",  "Finger Hands Finger Puppets"]

driver.get("https://www.amazon.com/")
driver.maximize_window()
time.sleep(2)
time.sleep(3)
driver.execute_script("window.scrollTo(0, 300)") 
time.sleep(4)
driver.execute_script("window.scrollTo(300, 600)") 
inputElement = driver.find_element_by_tag_name("body")
inputElement.send_keys(Keys.TAB * 3, Keys.ENTER)
time.sleep(3)
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
driver.close()
