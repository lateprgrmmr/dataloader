import logging
import pandas as pd
import os
import re
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from googlesearch import search

logging.getLogger('scrapy').propagate = False

def get_urls(tag, n, language):
    urls = [url for url in search(tag, stop=n, lang=language)][:n]
    print(urls)
    return urls

if __name__ == "__main__":
    get_urls('Funeral Home in Boise, ID', 50, 'en')
