# import time
from csv import reader
# import csv
import pandas as pd


# import re
import urllib.request as ur
from bs4 import BeautifulSoup as bs  # , SoupStrainer
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# url = "https://meritmemorial.com/obituaries"

# driver = webdriver.Chrome()
# driver.get(url)
# time.sleep(3)

# obit_links = []
# frame = driver.find_element_by_tag_name('iframe')
# driver.switch_to.frame(frame)
# i = 1
# while i in range(1,53):
#     elems = driver.find_elements_by_xpath('//a[@href]')
#     for elem in elems:
#         e = elem.get_attribute('href')
#         t = elem.text
#         if re.search('/tribute/details', e) and e not in obit_links:
#             obit_links.append(f'pg. {i},{e},{t}')
#     driver.find_element_by_class_name('next-page').click()
#     i = i + 1
#         # print(elem.get_attribute('href'))
# # print(obit_links, len(obit_links))
# with open('obit_links.csv', 'w') as f:
#     f.write('\n'.join(obit_links))
# driver.quit()
obit_text = []
PARSER = 'html.parser'
with open('Merit_obitlinks.csv', 'r') as f:
    csv_reader = reader(f)
    header = next(csv_reader)
    if header is not None:
        for row in csv_reader:
            # print(row)
            resp = ur.urlopen(row[2])
            soup = bs(resp, PARSER)
            link = soup.find('div', attrs={'class': 'obituary-plain-text'})
            # field_names = ['id', 'decedent', 'obit_text']
            try:
                obit_text.append([row[0], row[1], link.text])
            except AttributeError:
                obit_text.append([row[0], row[1], link])
df = pd.DataFrame(obit_text, columns=['id', 'decedent', 'obit_text'])
df.to_csv('out_text.csv')
# print(obit_text)
