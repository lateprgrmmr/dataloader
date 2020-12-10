import glob
# import petl as etl
# import csv
# from collections import OrderedDict
import pandas as pd
# import usaddress as us
# import numpy as np

m = {
    'Recipient': 'name',
    'AddressNumber': 'street1',
    'AddressNumberPrefix': 'street1',
    'AddressNumberSuffix': 'street1',
    'SecondStreetName': 'street1',
    'SecondStreetNamePostType': 'street1',
    'StreetName': 'street1',
    'StreetNamePreDirectional': 'street1',
    'StreetNamePreModifier': 'street1',
    'StreetNamePreType': 'street1',
    'StreetNamePostDirectional': 'street1',
    'StreetNamePostModifier': 'street1',
    'StreetNamePostType': 'street1',
    'CornerOf': 'street1',
    'IntersectionSeparator': 'street1',
    'LandmarkName': 'street1',
    'USPSBoxGroupID': 'street1',
    'USPSBoxGroupType': 'street1',
    'USPSBoxID': 'street1',
    'USPSBoxType': 'street1',
    'BuildingName': 'street2',
    'OccupancyType': 'street2',
    'OccupancyIdentifier': 'street2',
    'SubaddressIdentifier': 'street2',
    'SubaddressType': 'street2',
    'PlaceName': 'city',
    'StateName': 'state',
    'ZipCode': 'zip',
}

all_states = pd.DataFrame()
for f in glob.glob('/Users/kevinbratt/Downloads/NOMIS data/*'):
    df = pd.read_excel(f)
    all_states = all_states.append(df, ignore_index=True)
# com = all_states.to_excel('AllData.xlsx')
t1 = all_states.replace(to_replace='\n', value='$', regex=True)
t1.to_excel('AllData-New.xlsx')

# a = pd.read_csv('spadd.csv')
# all_address = []
# for row in a['address']:
#     p = us.tag(row, tag_mapping=m)
#     all_address.append(p)
# b = pd.DataFrame(all_address)
# b.to_csv('outagain.csv')
