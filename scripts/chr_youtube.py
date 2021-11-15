from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random


driver = webdriver.Chrome('C:/Users/Moisés/Desktop/chromedriver')

driver.maximize_window()
driver.get("https://www.youtube.com/")
time.sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
actions = driver.find_element_by_tag_name('body');  
actions.send_keys(Keys.TAB * 4, Keys.ENTER)



driver.get("https://www.youtube.com/results?search_query=Drive+Drive+Drive+song+(Impractical+Jokers)+-+2+HOUR+VERSION")
time.sleep(5)
inputElement = driver.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]")
inputElement.click()


time.sleep(400)
driver.close()
