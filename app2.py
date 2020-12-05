from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests

browser = webdriver.Chrome()
browser.get('http://www.google.com/maps')

TERM = 'Cloverdale Funeral Home'

search = browser.find_element_by_name('q')
search.send_keys(TERM)
search.send_keys(Keys.RETURN)

W = 'http://www.google.com/maps/place/Cloverdale+Funeral+Home,+Cemetery+and+Cremation/'
pth = requests.get(W)
soup = BeautifulSoup(pth.text, 'lxml')
a = soup.find("pane", {"class": "ugiz4pqJLAG__primary-text gm2-body-2"})
print(a)
#print(soup.prettify())
#time.sleep(5)

#  <div jstcache="741" class="ugiz4pqJLAG__primary-text gm2-body-2" jsan="7.ugiz4pqJLAG__primary-text,7.gm2-body-2">1200 N Cloverdale Rd, Boise, ID 83713</div>