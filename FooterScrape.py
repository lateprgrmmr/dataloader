# import selenium
import re
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
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
    tic = time.perf_counter()
    option = Options()
    option.add_argument('headless')
    driver = webdriver.Chrome(options=option)
    driver.get(s)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    if soup.find_all(href=re.compile('funeralone')) != []:
        RES.append([s, 'FuneralOne']) #,soup.find_all(href=re.compile('funeralone'))])
    elif soup.find_all(href=re.compile('funeraltech')) != []:
        RES.append([s, 'FuneralTech']) #,soup.find_all(href=re.compile('funeraltech'))])
    elif soup.find_all(href=re.compile('srscomputing')) != []:
        RES.append([s, 'SRS']) #,soup.find_all(href=re.compile('srscomputing'))])
    elif soup.find_all(href=re.compile('frazerconsultants')) != []:
        RES.append([s, 'Frazer Consultants'])
        #,soup.find_all(href=re.compile('frazerconsultants'))])
    elif soup.find_all(href=re.compile('consolidatedfuneralservices')) != []:
        RES.append([s, 'CFS']) #,soup.find_all(href=re.compile('consolidatedfuneralservices'))])
    elif soup.find_all(href=re.compile('funeralinnovations')) != []:
        RES.append([s, 'Funeral Innovations'])
        #,soup.find_all(href=re.compile('funeralinnovations'))])
    elif soup.find_all(href=re.compile('frontrunner360')) != []:
        RES.append([s, 'FrontRunner']) #,soup.find_all(href=re.compile('frontrunner360'))])
    elif soup.find_all(href=re.compile('batesvilletechnology')) != []:
        RES.append([s, 'Batesville']) #,soup.find_all(href=re.compile('batesvilletechnology'))])
    elif soup.find_all(href=re.compile('funeralresults')) != []:
        RES.append([s, 'FRM']) #,soup.find_all(href=re.compile('funeralresults'))])
    else:
        RES.append([s, 'Could not determine provider'])
    driver.close()
    toc = time.perf_counter()
    tt = toc - tic
    RES.append(tt)
print(RES)
