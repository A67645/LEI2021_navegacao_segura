from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random


driver = webdriver.Chrome('C:/Users/Moisés/Desktop/chromedriver')

word_list=["stack overflow how to capture traffic", "p2p network"]
driver.get("https://www.google.com/")
driver.maximize_window()
time.sleep(1)
actions = driver.find_element_by_tag_name('body');  
actions.send_keys(Keys.TAB * 5, Keys.ENTER)
time.sleep(3)
inputElement = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
inputElement.send_keys(random.choice(word_list), Keys.ENTER)

time.sleep(3)
element = driver.find_element_by_xpath("/html/body/div[7]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[1]/a")
time.sleep(1)
driver.get(element.get_attribute('href'))
time.sleep(1)
lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")

time.sleep(4)
driver.close()

