from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.keys import Keys
import time
import random

options = EdgeOptions()
options.use_chromium = True

driver = Edge(options=options)
driver.get("https://www.facebook.com/")
driver.maximize_window()
time.sleep(1)
actions = driver.find_element_by_tag_name('body');  
actions.send_keys(Keys.TAB * 4, Keys.ENTER)
#actions.click()
#actions.send_keys(Keys.ENTER)
time.sleep(1)
inputElement = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input")
inputElement.send_keys('armaldo.franciso@gmail.com')
time.sleep(3)
inputElement = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input")
inputElement.send_keys('passwordfraca', Keys.ENTER)
time.sleep(3)

driver.get("https://www.facebook.com/")
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
driver.close()
