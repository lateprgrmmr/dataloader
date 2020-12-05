import requests

r = requests.get('https://www.google.com/maps/place/Cloverdale+Funeral+Home,+Cemetery+and+Cremation/@43.6174474,-116.3339063,17z/data=!3m1!4b1!4m5!3m4!1s0x54ae542f72ac6b5f:0x15224a514751ab24!8m2!3d43.6174435!4d-116.3317176')
print(r)