import xml.etree.ElementTree as et

XMLfile = '/Users/kevinbratt/haughey.xml'


root = et.parse(XMLfile)
# result = {}
# caseList = []

# for e in root.findall('.//Case'):
#     if e.attrib.get('CaseId') != '':
#         if e.attrib.get('CaseId') not in result:
#             result['CaseID'] = e.attrib['CaseId']
#     if e.attrib.get('DeceasedName') != '':
#         if e.attrib.get('DeceasedName') not in result:
#             result['DeceasedName'] = e.attrib['DeceasedName']
#     if e.attrib.get('DOD') != '':
#         if e.attrib.get('DOD') not in result:
#             result['DOD'] = e.attrib['DOD']
#     # result.append(e)
#     if result not in caseList:
#         caseList.append(result)
# # print(f'{len(caseList)} cases in total.')
# print(caseList)

dic = {}
c = root.find('./Case')
dic['CaseId'] = c.attrib['CaseId']
caseElems = root.findall('./Case')
for a in caseElems[0]:
    y = a.findall('.//row')
    for j in y:
        u = j.find('./ci_Addresses')
        # print(u)
        if u is not None:
            addG = u.attrib['AddrGUID']
            caseG = u.attrib['CaseGUID']
            dic['AddrGUID'] = addG
            dic['CaseGUID'] = caseG
            dic['FirstName'] = u.attrib['FirstName']
            dic['MiddleName'] = u.attrib['MiddleName']
            dic['LastName'] = u.attrib['LastName']
            dic['Address1'] = u.attrib['Address1']
            dic['Address2'] = u.attrib['Address2']
            dic['City'] = u.attrib['City']
            dic['State'] = u.attrib['State']
            dic['Zip'] = u.attrib['Zip']
            dic['SSNumber'] = u.attrib['SSNumber']
            dic['DateOfBirth'] = u.attrib['DateOfBirth']
            dic['DateOfDeath'] = u.attrib['DateOfDeath']


c = root.find(f'[@CaseGUID="{caseG}"]')  # '[@CaseGUID="4A0EB798-B7C8-4951-9814-8794F9CA20E4"]')
if c is not None:
    dic['CaseId'] = c.attrib['CaseId']

print(dic)
