import pandas as pd
import usaddress as us

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

ADDRESS = []
data = pd.read_csv('address.csv', dtype='string')
for row in data['description']:
    try:
        b = us.tag(str(row), tag_mapping=m)
        # w = [b[0]['street1'], b[0]['street1'], b[0]['street2'],
        #      b[0]['city'], b[0]['state'], b[0]['zip']]
        w = [b[0]]
        ADDRESS.append(w)
    except us.RepeatedLabelError as e:
        n = 'Check Address'
        ADDRESS.append(n)
    fixed = pd.DataFrame(ADDRESS, columns=['fh_name',
                                           'address1',
                                           'address2',
                                           'city',
                                           'state',
                                           'postal_code'])
o = pd.DataFrame(fixed)
o.to_csv('parsed_addresses.csv')
