# from googlemaps import GoogleMaps
# api_key = 'AIzaSyCVYk4lbdTojFq9Ep7OnOr-PJavtZwFuf8'

# gmaps = GoogleMaps(api_key)
# local = gmaps.local_search(fh_name)
# print(local['responseData']['results'][0]['titleNoFormatting'])

import googlemaps
gmaps = googlemaps('AIzaSyCVYk4lbdTojFq9Ep7OnOr-PJavtZwFuf8')
local = gmaps.local_search('sushi san francisco, ca')
result = local['responseData']['results'][0]
print(result['titleNoFormatting'])