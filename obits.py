import time
import csv

import re
import urllib.request as ur
from bs4 import BeautifulSoup as bs  # , SoupStrainer
from selenium import webdriver
from selenium.webdriver.common.by import By

# PARSER = 'html5lib'
# resp = ur.urlopen("https://meritmemorial.com/obituaries")
# soup = bs(resp, PARSER)
# for link in soup.find_all('a', attrs={'href': re.compile(
# "^/tribute/details")}): #/tribute/details")}):
#     print(link['href'])
# print(soup.prettify())
url = "https://meritmemorial.com/obituaries"

driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)
# page = driver.page_source
# driver.quit()
# soup = bs(page, 'html.parser')
# DIV = range(10)
# for i in DIV:
#     var = i + 1
#     container = soup.find(By.XPATH, f'//*[@id="arrangement-list-full"]/div[2]/div[{var}]/div[2]/h2/a')
#     print(f'Oh, "var" is {var}', container.href)
# driver.find_element_by_xpath('//*[@id="arrangement-list-full"]/div[2]/div[1]/div[2]/h2/a')

# elems = driver.find_elements_by_xpath('//a[@href]')
# for elem in elems:
    # print(elem.get_attribute('href'))
obit_links = []
frame = driver.find_element_by_tag_name('iframe')
driver.switch_to.frame(frame)
i = 1
while i in range(1,53):
    elems = driver.find_elements_by_xpath('//a[@href]')
    for elem in elems:
        e = elem.get_attribute('href')
        t = elem.text
        if re.search('/tribute/details', e) and e not in obit_links:
            obit_links.append(f'pg. {i},{e},{t}')
    driver.find_element_by_class_name('next-page').click()
    i = i + 1
        # print(elem.get_attribute('href'))
# print(obit_links, len(obit_links))
with open('obit_links.csv', 'w') as f:
    f.write('\n'.join(obit_links))
driver.quit()