import requests
from bs4 import BeautifulSoup as bs
import re

URL = 'https://www.relyeafuneralchapel.com/tributes'
page = requests.get(URL)

soup = bs(page.content, 'html.parser')
results = soup.find(id='obitlist')

obits = {}
obit_elems = results.find_all('div', class_='col-sm-9 col-xs-8')
for obit_elem in obit_elems:
    decedent_name = obit_elem.find('span', class_='obitlist-title')
    url_suff = obit_elem.find('a')
    obit_link = URL + "".join(url_suff.get('href').split('/tributes')[1:])
    obits.update({decedent_name.text.strip() : URL + "".join(url_suff.get('href').split('/tributes')[1:])})
    #print(decedent_name.text.strip(), URL + "".join(url_suff.get('href').split('/tributes')[1:]))
    #print(URL + "".join(url_suff.get('href').split('/tributes')[1:]))
    #print(decedent_name, obit_text)
    #print(obit_elem, end='\n'*2)
    #print(obits)
for k, v in obits.items():
    page = requests.get(v)

    soup = bs(page.content, 'html.parser')
    results = soup.find(id='obcontent')
    obit_text = results.find('div', id='obtext')
    print(k, "".join(obit_text.text.strip().split('Tribute')), sep='\n', end='\n' * 2)
