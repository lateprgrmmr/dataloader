from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('http://www.google.com/maps')

search_term = 'Robert E. Decker Funeral Home'

search = browser.find_element_by_name('q')
search.send_keys(search_term)
search.send_keys(Keys.RETURN)

#time.sleep(5)

