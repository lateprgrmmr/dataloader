import usaddress as us
import easypost as ep
import pandas as pd

#easypost.api_key = "EZTKece6bf0ff0fa48bf8da13fa4196afd16f8dyDUj8fqj0AtdYj0jmuQ"

Recipient = []
addresses = []
a = pd.read_csv('address.csv', index_col="Company ID")
