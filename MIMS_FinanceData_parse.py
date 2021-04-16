import xml.sax
from enum import Enum
import pandas as pd
import json
from json2html import *
import sys


def eprint(str):
    sys.stderr.write(f"{str}\n")


class MIMS(Enum):
    START = 0
    MIMSDB = 1
    CASE = 2
    # CICASEDATA = 3
    CIFINANCE = 4
    CIALTERATIONS = 5
    CIAUTOMOTIVE = 6
    CICASHADVANCE = 7
    CIFACILITIES = 8
    CIMERCHANDISE = 9
    END = 1000


class MIMSHandler(xml.sax.ContentHandler):

    def __init__(self):
        self.state = MIMS.START
        self.currentCase = {}
        self.fin = {}
        self.altList = []
        self.alt = {}
        self.autoList = []
        self.auto = {}
        self.cashList = []
        self.cash = {}
        self.facList = []
        self.fac = {}
        self.merchList = []
        self.merch = {}
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
            self.currentCase['CaseGUID'] = attrs['CaseGUID'].upper()
            self.currentCase['case_number'] = attrs['CaseId']
        elif self.state == MIMS.CASE and name == 'ci_Finance':
            self.state = MIMS.CIFINANCE
        elif self.state == MIMS.CIFINANCE and name == 'row':
            self.fin['FinGUID'] = attrs['FinGUID']
            self.fin['CaseGUID'] = attrs['CaseGUID']
            self.fin['DateContract'] = attrs['DateContract']
            self.fin['TotalGlobal'] = attrs['TotalGlobal']
            self.fin['Total'] = attrs['Total']
            self.fin['TotalCashAdvances'] = attrs['TotalCashAdvances']
            self.fin['TotalAlterations'] = attrs['TotalAlterations']
            self.currentCase['Finance'] = self.fin
        elif self.state == MIMS.CASE and name == 'ci_fin_Alterations':
            self.state = MIMS.CIALTERATIONS
        elif self.state == MIMS.CIALTERATIONS and name == 'row':
            intAlt = {}
            intAlt['FinGUID'] = attrs['FinGUID']
            intAlt['AltGUID'] = attrs['AltGUID']
            if 'Description' in attrs:
                intAlt['Description'] = attrs['Description']
            if 'Price' in attrs:
                intAlt['Price'] = attrs['Price']
            if 'Category' in attrs:
                intAlt['Category'] = attrs['Category']
            if 'Deleted' in attrs:
                intAlt['Deleted'] = attrs['Deleted']
            self.altList.append(intAlt)
            self.alt['Alterations'] = self.altList
            self.currentCase['Alterations'] = self.altList
        elif self.state == MIMS.CASE and name == 'ci_fin_Automotive':
            self.state = MIMS.CIAUTOMOTIVE
        elif self.state == MIMS.CIAUTOMOTIVE and name == 'row':
            intAuto = {}
            if 'FinGUID' in attrs:
                intAuto['FinGUID'] = attrs['FinGUID']
            if 'AutoGUID' in attrs:
                intAuto['AutoGUID'] = attrs['AutoGUID']
            if 'Label' in attrs:
                intAuto['Label'] = attrs['Label']
            if 'Total' in attrs:
                intAuto['Total'] = attrs['Total']
            if 'Deleted' in attrs:
                intAuto['Deleted'] = attrs['Deleted']
            self.autoList.append(intAuto)
            self.auto['Automotive'] = self.autoList
            self.currentCase['Automotive'] = self.auto
        elif self.state == MIMS.CASE and name == 'ci_fin_CashAdvance':
            self.state = MIMS.CICASHADVANCE
        elif self.state == MIMS.CICASHADVANCE and name == 'row':
            intCash = {}
            if 'FinGUID' in attrs:
                intCash['FinGUID'] = attrs['FinGUID']
            if 'CashAdvGUID' in attrs:
                intCash['CashAdvGUID'] = attrs['CashAdvGUID']
            if 'Description' in attrs:
                intCash['Description'] = attrs['Description']
            if 'Total' in attrs:
                intCash['Total'] = attrs['Total']
            if 'Deleted' in attrs:
                intCash['Deleted'] = attrs['Deleted']
            self.cashList.append(intCash)
            self.cash['Cash'] = self.cashList
            self.currentCase['Cash'] = self.cash
        elif self.state == MIMS.CASE and name == 'ci_fin_Facilities':
            self.state = MIMS.CIFACILITIES
        elif self.state == MIMS.CIFACILITIES and name == 'row':
            intFac = {}
            if 'FinGUID' in attrs:
                intFac['FinGUID'] = attrs['FinGUID']
            if 'FacGUID' in attrs:
                intFac['FacGUID'] = attrs['FacGUID']
            if 'Label' in attrs:
                intFac['Label'] = attrs['Label']
            if 'Total' in attrs:
                intFac['Total'] = attrs['Total']
            if 'Deleted' in attrs:
                intFac['Deleted'] = attrs['Deleted']
            self.facList.append(intFac)
            self.fac['Facilities'] = self.facList
            self.currentCase['Facilities'] = self.fac
        elif self.state == MIMS.CASE and name == 'ci_fin_Merchandise':
            self.state = MIMS.CIMERCHANDISE
        elif self.state == MIMS.CIMERCHANDISE and name == 'row':
            intMerch = {}
            if 'FinGUID' in attrs:
                intMerch['FinGUID'] = attrs['FinGUID']
            if 'MerchGUID' in attrs:
                intMerch['MerchGUID'] = attrs['MerchGUID']
            if 'Label' in attrs:
                intMerch['Label'] = attrs['Label']
            if 'Supplier' in attrs:
                intMerch['Supplier'] = attrs['Supplier']
            if 'Description1' in attrs:
                intMerch['Description1'] = attrs['Description1']
            if 'Description2' in attrs:
                intMerch['Description2'] = attrs['Description2']
            if 'KindOfMetal' in attrs:
                intMerch['KindOfMetal'] = attrs['KindOfMetal']
            if 'Model' in attrs:
                intMerch['Model'] = attrs['Model']
            if 'Color' in attrs:
                intMerch['Color'] = attrs['Color']
            if 'Emblem' in attrs:
                intMerch['Emblem'] = attrs['Emblem']
            if 'ExteriorColor' in attrs:
                intMerch['ExteriorColor'] = attrs['ExteriorColor']
            if 'Quantity' in attrs:
                intMerch['Quantity'] = attrs['Quantity']
            if 'Cost' in attrs:
                intMerch['Cost'] = attrs['Cost']
            if 'Price' in attrs:
                intMerch['Price'] = attrs['Price']
            if 'Deleted' in attrs:
                intMerch['Deleted'] = attrs['Deleted']
            self.merchList.append(intMerch)
            self.merch['Merchandise'] = self.merchList
            self.currentCase['Merchandise'] = self.merch
        else:
            eprint(f"UNHANDLED <{name}> FROM STATE {self.state}")

    def endElement(self, name):
        eprint(f"<<IN STATE: {self.state}\t\tEND ELEMENT: <{name}>")
        if name == 'MIMSDB':
            self.state = MIMS.END
            eprint("All done!")
        elif name == 'Case':
            # print(f'Case: {self.currentCase}\n\n')
            # print(f'Addresses....: {self.addrInfo}\n')
            # print(f'Current Case: {self.currentCase}\n')
            # print(f'Finance: {self.fin}\n')
            # if self.auto != {}:
            #     print(f'Contract Alterations: {self.alt}\n')
            # else:
            #     print('No Contract Alterations\n\n')
            # if self.auto != {}:
            #     print(f'Automotive Charges: {self.auto}\n')
            # else:
            #     print('No Automotive Charges\n\n')
            # if self.cash != {}:
            #     print(f'Cash Advances: {self.cash}\n')
            # else:
            #     print('No Cash Advances\n\n')
            # if self.fac != {}:
            #     print(f'Facilities Charges: {self.fac}\n')
            # else:
            #     print('No Facilities Charges\n\n')
            # if self.merch != {}:
            #     print(f'Selected Merchandise: {self.merch}\n')
            # else:
            #     print('No Merchandise\n\n')
            jOut = json.dumps(self.currentCase)
            with open('json_test.html', 'w') as o:
                o.write(json2html.convert(jOut))
            self.currentCase = {}
            self.fin = {}
            self.altList = []
            self.alt = {}
            self.autoList = []
            self.auto = {}
            self.cashList = []
            self.cash = {}
            self.facList = []
            self.fac = {}
            self.merchList = []
            self.merch = {}
            self.state = MIMS.MIMSDB
        elif name == 'ci_Finance':
            self.state = MIMS.CASE
        elif name == 'ci_fin_Alterations':
            self.state = MIMS.CASE
        elif name == 'ci_fin_Automotive':
            self.state = MIMS.CASE
        elif name == 'ci_fin_CashAdvance':
            self.state = MIMS.CASE
        elif name == 'ci_fin_Facilities':
            self.state = MIMS.CASE
        elif name == 'ci_fin_Merchandise':
            self.state = MIMS.CASE
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
