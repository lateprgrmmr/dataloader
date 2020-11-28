import usaddress as us
import easypost as ep
#import pandas as pd
import petl as etl
#import csv

ep.api_key = "EZTKece6bf0ff0fa48bf8da13fa4196afd16f8dyDUj8fqj0AtdYj0jmuQ"
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

# ez = (
#     ['delivery']: 'verify',
#     ['street1']: 'street1',
#     ['street2']: 'street2',
#     ['city']: 'city',
#     ['state']: 'state',
#     ['zip']: 'zip',
# )
T1 = etl.fromcsv('address1.csv')
#print(T2)
T2 = etl.convert(T1, 'Street Address', lambda x: us.tag(x.title(), m))
T3 = etl.convert(T2, 'Street Address', lambda y: type(y))
etl.tocsv(T3, 'testing.csv')
