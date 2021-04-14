import xml.sax
from enum import Enum
import pandas as pd
import sys


def eprint(str):
    sys.stderr.write(f"{str}\n")


class MIMS(Enum):
    START = 0
    MIMSDB = 1
    CASE = 2
    CIADDRESSES = 3
    CICASEDATA = 4
    CISURVIVORS = 5
    END = 1000


class MIMSHandler(xml.sax.ContentHandler):

    def __init__(self):
        self.state = MIMS.START
        self.currentCase = {}
        self.addrInfo = {}
        self.caseList = []
        self.inf = ''
        self.cases = pd.DataFrame(columns=['CaseGUID', 'case_number',
                                           'fname', 'mname', 'lname', 'email',
                                           'phone', 'relationship', 'address1',
                                           'address2', 'city', 'state',
                                           'postal_code', 'country'])

    def startElement(self, name, attrs):
        eprint(f">>IN STATE: {self.state}\t\tSTART ELEMENT: <{name}>")
        if self.state == MIMS.START and name == 'MIMSDB':
            self.state = MIMS.MIMSDB
        elif self.state == MIMS.MIMSDB and name == 'Case':
            self.state = MIMS.CASE
            self.currentCase['CaseGUID'] = attrs['CaseGUID']
            self.currentCase['case_number'] = attrs['CaseId']
            self.currentCase['helpers'] = self.caseList
        elif self.state == MIMS.CASE and name == 'ci_CaseData':
            self.state = MIMS.CICASEDATA
        elif self.state == MIMS.CICASEDATA and name == 'row':
            if 'FatherGUID' in attrs and attrs['FatherGUID'] != '00000000-0000-0000-0000-000000000000':
                self.caseList.append({'relation': 'father', 'GUID': attrs['FatherGUID']})
            if 'MotherGUID' in attrs and attrs['MotherGUID'] != '00000000-0000-0000-0000-000000000000':
                self.caseList.append({'relation': 'mother', 'GUID': attrs['MotherGUID']})
            if 'SpouseGUID' in attrs and attrs['SpouseGUID'] != '00000000-0000-0000-0000-000000000000':
                self.caseList.append({'relation': 'spouse', 'GUID': attrs['SpouseGUID']})
            if 'InformantGUID' in attrs and attrs['InformantGUID'] != '00000000-0000-0000-0000-000000000000':
                self.caseList.append({'relation': attrs['InfRelation'].strip().lower(), 'GUID': attrs['InformantGUID']})
                self.inf = attrs['InformantGUID']
                # print(inf)
        elif self.state == MIMS.CASE and name == 'ci_Survivors':
            self.state = MIMS.CISURVIVORS
        elif self.state == MIMS.CISURVIVORS and name == 'row':
            if 'SurvGUID' in attrs and 'Relation' in attrs:
                self.caseList.append({'relation': attrs['Relation'].strip().lower(), 'GUID': attrs['AddrGUID']})
        elif self.state == MIMS.CASE and name == 'ci_Addresses':
            self.state = MIMS.CIADDRESSES
        elif self.state == MIMS.CIADDRESSES and name == 'row':
            addr = {}
            addr['CaseGUID'] = self.currentCase['CaseGUID']
            addr['case_number'] = self.currentCase['case_number']
            if 'AddrGUID' in attrs:
                addr['AddrGUID'] = attrs['AddrGUID']
            if 'FirstName' in attrs:
                addr['fname'] = attrs['FirstName']
            if 'MiddleName' in attrs:
                addr['mname'] = attrs['MiddleName']
            if 'LastName' in attrs:
                addr['lname'] = attrs['LastName']
            if 'EMail' in attrs:
                addr['email'] = attrs['EMail']
            if 'Phone' in attrs:
                addr['phone'] = attrs['Phone']
            if 'Address1' in attrs:
                addr['address1'] = attrs['Address1']
            if 'Address2' in attrs:
                addr['address2'] = attrs['Address2']
            if 'City' in attrs:
                addr['city'] = attrs['City']
            if 'State' in attrs:
                addr['state'] = attrs['State']
            if 'Zip' in attrs:
                addr['postal_code'] = attrs['Zip']
            if 'Country' in attrs:
                addr['country'] = attrs['Country']
            addr['is_informant'] = self.inf
            self.addrInfo[attrs['AddrGUID']] = addr
        else:
            eprint(f"UNHANDLED <{name}> FROM STATE {self.state}")

    def endElement(self, name):
        eprint(f"<<IN STATE: {self.state}\t\tEND ELEMENT: <{name}>")
        if name == 'MIMSDB':
            self.state = MIMS.END
            eprint("All done!")
        elif name == 'Case':
            # print(f'Case: {self.currentCase}\n')
            # print(f'Addresses....: {self.addrInfo}\n')
            for i in self.caseList:
                if i['GUID'] in self.addrInfo:
                    address = self.addrInfo[i['GUID']]
                    address['relationship'] = i['relation']
                    # print(address)  #, i['relation'], self.currentCase['case_number'])
            # print(f'Helpers: {self.currentCase["helpers"]}\n')
            # Do something with the currentCase (other than just print it)
                self.cases = self.cases.append(address, ignore_index=True)
            self.cases.to_csv('HelpOut.csv')
            # print(self.cases)
            self.currentCase = {}
            self.addrInfo = {}
            self.caseList = []
            self.state = MIMS.MIMSDB
        elif name == 'ci_Addresses':
            self.state = MIMS.CASE
        elif name == 'ci_CaseData':
            self.state = MIMS.CASE
        elif name == 'ci_Survivors':
            self.state = MIMS.CASE
            # eprint(self.survivors)
        elif name == 'row':
            self.state = self.state  # basically a noop
        else:
            eprint(f"UNHANDLED END <{name}> STAYING IN STATE {self.state}")


if (__name__ == "__main__"):
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    Handler = MIMSHandler()
    parser.setContentHandler(Handler)
    parser.parse('/Users/kevinbratt/haugheyFormat.xml')
