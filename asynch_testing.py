import csv
import re
import time

import grequests
from bs4 import BeautifulSoup

# import requests

start_time = time.time()

# URLS = [
#     'https://jwfuneraldirectors.net/',
#     'https://www.nswcares.com/',
#     'https://bellbrothersfuneral.com/',
#     'https://www.bondfuneraldirectors.com/'
# ]

RES = []
with open('atest.csv', 'r') as URLS:
    reqs = (grequests.get(link) for link in URLS)
    resp = grequests.imap(reqs, grequests.Pool(10))


    for r in resp:
        soup = BeautifulSoup(r.text, 'lxml')
        if soup.find_all(href=re.compile('funeralone')) != []:
            # ,soup.find_all(href=re.compile('funeralone'))])
            RES.append([r.url, 'FuneralOne'])
        elif soup.find_all(href=re.compile('funeraltech')) != []:
            # ,soup.find_all(href=re.compile('funeraltech'))])
            RES.append([r.url, 'FuneralTech'])
        elif soup.find_all(href=re.compile('srscomputing')) != []:
            # ,soup.find_all(href=re.compile('srscomputing'))])
            RES.append([r.url, 'SRS'])
        elif soup.find_all(href=re.compile('frazerconsultants')) != []:
            RES.append([r.url, 'Frazer Consultants'])
            # ,soup.find_all(href=re.compile('frazerconsultants'))])
        elif soup.find_all(href=re.compile('consolidatedfuneralservices')) != []:
            # ,soup.find_all(href=re.compile('consolidatedfuneralservices'))])
            RES.append([r.url, 'CFS'])
        elif soup.find_all(href=re.compile('funeralinnovations')) != []:
            RES.append([r.url, 'Funeral Innovations'])
            # ,soup.find_all(href=re.compile('funeralinnovations'))])
        elif soup.find_all(href=re.compile('frontrunner360')) != []:
            # ,soup.find_all(href=re.compile('frontrunner360'))])
            RES.append([r.url, 'FrontRunner'])
        elif soup.find_all(href=re.compile('batesvilletechnology')) != []:
            # ,soup.find_all(href=re.compile('batesvilletechnology'))])
            RES.append([r.url, 'Batesville'])
        elif soup.find_all(href=re.compile('funeralresults')) != []:
            # ,soup.find_all(href=re.compile('funeralresults'))])
            RES.append([r.url, 'FRM'])
        else:
            RES.append([r.url, 'Could not determine provider'])
        tt = time.time() - start_time
        RES.append(tt)
print(RES)

