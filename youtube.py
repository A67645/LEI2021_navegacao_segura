from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.keys import Keys
import time

options = EdgeOptions()
options.use_chromium = True

driver = Edge(options=options)
driver.get("https://www.youtube.com/")
driver.maximize_window()
time.sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
actions = driver.find_element_by_tag_name('body');  
actions.send_keys(Keys.TAB * 4, Keys.ENTER)
time.sleep(1)
actions = driver.find_element_by_tag_name('body');  
actions.send_keys(Keys.TAB * 3, Keys.ENTER)
#actions.click()
#actions.send_keys(Keys.ENTER)
time.sleep(1)
inputElement = driver.find_element_by_id("identifierId")
inputElement.send_keys('armaldo.franciso@gmail.com', Keys.ENTER)
time.sleep(3)
inputElement = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
inputElement.send_keys('passwordfraca', Keys.ENTER)
time.sleep(1)


driver.get("https://www.youtube.com/results?search_query=Drive+Drive+Drive+song+(Impractical+Jokers)+-+2+HOUR+VERSION")
time.sleep(1)
inputElement = driver.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]")
inputElement.click()


time.sleep(400)
driver.close()
