from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.keys import Keys
import time
import random

options = EdgeOptions()
options.use_chromium = True
word_list=["https://pt.wikipedia.org/wiki/Border_Gateway_Protocol",   "https://pt.wikipedia.org/wiki/Multi_Protocol_Label_Switching",   "https://pt.wikipedia.org/wiki/Open_Shortest_Path_First"]
driver = Edge(options=options)
driver.get("https://pt.wikipedia.org/")
driver.maximize_window()
time.sleep(5)
driver.get(random.choice(word_list))

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

