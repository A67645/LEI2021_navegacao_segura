from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.keys import Keys
import time
import random

options = EdgeOptions()
options.use_chromium = True



word_list=["stack overflow how to capture traffic",    "java display thread",  "p2p network"]
driver = Edge(options=options)
driver.get("https://www.google.com/")
driver.maximize_window()
time.sleep(1)
inputElement = driver.find_element_by_id("zV9nZe")
inputElement.click()
inputElement = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
inputElement.send_keys(random.choice(word_list), Keys.ENTER)

element = driver.find_element_by_xpath("/html/body/div[7]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div[1]/a")
time.sleep(1)
driver.get(element.get_attribute('href'))
time.sleep(1)
lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")

time.sleep(4)
driver.close()

