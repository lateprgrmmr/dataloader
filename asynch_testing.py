from csv import DictWriter
from concurrent.futures import ProcessPoolExecutor
import concurrent.futures


URLS = [
    'https://jwfuneraldirectors.net/',
    'https://www.nswcares.com/',
    'https://bellbrothersfuneral.com/',
    'https://www.bondfuneraldirectors.com/'
]

def parse(url):
    return data

results = []
for url in URLS:
    results.append(parse(url))

with open('results.csv', 'w') as f:
    writer = DictWriter(f, fieldnames=results[0].keys())
    writer.writeheader()
    writer.writerows(results)

