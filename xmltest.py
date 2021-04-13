import csv
import xml.etree.ElementTree as ET
from time import perf_counter


print('Start')
start = perf_counter()
tree = ET.parse('/Users/kevinbratt/haughey.xml')
MIMSDB = tree.getroot()
# Cases = MIMSDB.getchildren()  # Individual Case elements
tablesT = ['ci_Addresses', 'ci_CaseData', 'ci_DeathInfo', 'ci_Marketing',
           'ci_RacialInfo', 'ci_Service', 'ci_Survivors', 'ci_Finance',
           'ci_ServiceVisitation', 'su_PriceList', 'ci_fin_Automotive',
           'ci_fin_CashAdvance', 'ci_fin_Facilities', 'ci_fin_Merchandise',
           'su_PriceListFields', 'ci_OutOfTownArrangements',
           'ci_OTA_FlightInfo', 'ci_fin_Alterations', 'ci_Payments',
           'ci_SurvivorFollowup', 'ci_Preneed', 'ci_PNDepository',
           'ci_PNPayments', 'ci_Veteran', 'ci_Notes', 'ci_Checklist',
           'ci_CheckListLabels', 'ci_MerchandiseOrders',
           'ci_ContributionsTracking']
tables = []
# for table in tables:
#     tableFields = MIMSDB.findall('.//')
#     for each in tableFields:
#         rows = each.getchildren()
#         for row in rows:
#             for name in row.attrib:
#                 # if name not in fields:
#                 fields.append(table + '.' + name)
fields = []
ay = MIMSDB.getchildren()
for a in ay:
    for i in a:
        # print(i.tag)
        for j in i:
            for name in j.attrib:
                if (i.tag + '.' + name) not in fields:
                    fields.append(i.tag + '.' + name)
# for case in Cases[1]:
#     single = case.find('./row')
#     for name in single.attrib:
#         print(str(single) + '.' + name)
# out = []
# for case in Cases:
#     for table in case:
#         # out.append(table.getchildren())
#         print(table)
#         for name in table.attrib:
#             print('{0}="{1}"'.format(name, table.attrib[name]))
        # for row in table:
            # for name in row.attrib:
            #     print('{0}="{1}"'.format(name, row.attrib[name]))

# tables = []
# for i in out:
#     if i not in tables:
#         tables.append(i)
# print(tables)
print('Fields = ', fields)
stop = perf_counter()
elapsed = stop - start
print('Stop. Took: ' + str(elapsed))
