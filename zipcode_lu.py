# import csv
from pyzipcode import ZipCodeDatabase

zd = ZipCodeDatabase()
zipcode = zd[83646]
zipcode.zip
# lists = []
# with open('zips.csv') as f:
#     reader = csv.reader(f, delimiter=',')
#     for row in reader:
#         u = zd[row[1]]
#         lists.append(row, u)
# print(lists)

