# import selenium
import re
from selenium import webdriver
# import requests
from bs4 import BeautifulSoup


SEARCH = [
    'https://jwfuneraldirectors.net/',
    'https://www.nswcares.com/',
    'https://bellbrothersfuneral.com/',
    'https://www.bondfuneraldirectors.com/'
]

RES = []

for s in SEARCH:
    driver = webdriver.Chrome()
    driver.get(s)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    if soup.find_all(href=re.compile('funeralone')) != []:
        RES.append([s, 'FuneralOne'])#,soup.find_all(href=re.compile('funeralone'))])
    elif soup.find_all(href=re.compile('funeraltech')) != []:
        RES.append([s, 'FuneralTech'])#,soup.find_all(href=re.compile('funeraltech'))])
    elif soup.find_all(href=re.compile('srscomputing')) != []:
        RES.append([s, 'SRS'])#,soup.find_all(href=re.compile('srscomputing'))])
    else:
        RES.append([s, 'Could not determine provider'])
    driver.close()
print(RES)

