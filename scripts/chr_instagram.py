from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random


driver = webdriver.Chrome('C:/Users/Moisés/Desktop/chromedriver')
driver.get("https://www.instagram.com/")
driver.maximize_window()
time.sleep(3)
actions = driver.find_element_by_tag_name('body');  
actions.send_keys(Keys.TAB * 3, Keys.ENTER)
time.sleep(3)
inputElement = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
inputElement.send_keys("armaldoFransico",Keys.TAB,"criptografia", Keys.ENTER)
time.sleep(5)
actions = driver.find_element_by_tag_name('body');  
actions.send_keys(Keys.TAB , Keys.ENTER)

time.sleep(4)
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

