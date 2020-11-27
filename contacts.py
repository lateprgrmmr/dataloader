import usaddress as us
import easypost as ep
import pandas as pd
import easypost
import json
import csv

#easypost.api_key = "EZTKece6bf0ff0fa48bf8da13fa4196afd16f8dyDUj8fqj0AtdYj0jmuQ"

with open('address.csv', 'r') as address:
    for row in address:
        a = us.parse(row)
        print(a)


