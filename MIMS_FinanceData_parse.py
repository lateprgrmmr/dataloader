import xml.sax
from enum import Enum
# import pandas as pd
import json
from json2html import *
import datetime
import sys


headHTML = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    < title > """

styleHTML = """</title>

    <style>
        .invoice-box {
            max-width: 800px;
            margin: auto;
            padding: 30px;
            border: 1px solid #eee;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.15);
            font-size: 16px;
            line-height: 24px;
            font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;
            color: #555;
        }

        .invoice-box table {
            width: 100%;
            line-height: inherit;
            text-align: left;
            border-collapse: collapse !important;
            border-bottom: 1px black !important;
        }

        .invoice-box table tr td:hover {
            background-color: #cdcfca;
        }
        .invoice-box table td {
            padding: 5px;
            vertical-align: top;
        }

        .invoice-box table tr td:nth-child(2) {
            text-align: right;
        }

        .invoice-box table tr.top table td {
            padding-bottom: 20px;
        }

        .invoice-box table tr.top table td.title {
            font-size: 45px;
            line-height: 45px;
            color: #333;
        }

        .invoice-box table tr.information table td {
            padding-bottom: 40px;
        }

        .invoice-box table tr.heading td {
            background: #eee;
            border-bottom: 1px solid #ddd;
            font-weight: bold;
        }

        .invoice-box table tr.details td {
            padding-bottom: 20px;
        }

        .invoice-box table tr.item td {
            border-bottom: 1px solid #eee;
        }

        .invoice-box table tr.item.last td {
            border-bottom: none;
        }

        .invoice-box table tr.total td:nth-child(2) {
            border-top: 2px solid #eee;
            font-weight: bold;
        }

        @media only screen and (max-width: 600px) {
            .invoice-box table tr.top table td {
                width: 100%;
                display: block;
                text-align: center;
            }

            .invoice-box table tr.information table td {
                width: 100%;
                display: block;
                text-align: center;
            }
        }

        /** RTL **/
        .rtl {
            direction: rtl;
            font-family: Tahoma, 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;
        }

        .rtl table {
            text-align: right;
        }

        .rtl table tr td:nth-child(2) {
            text-align: left;
        }
    </style>
</head>

<body>
    <div class="invoice-box">
"""

tailHTML = """
    </div>
</body>
</html>
"""


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
        self.finList = []
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
        # self.cases = pd.DataFrame(columns=['CaseGUID', 'case_number',
        #                                    'fname', 'mname', 'lname', 'email',
        #                                    'phone', 'relationship', 'address1',
        #                                    'address2', 'city', 'state',
        #                                    'postal_code', 'country'])

    def startElement(self, name, attrs):
        eprint(f">>IN STATE: {self.state}\t\tSTART ELEMENT: <{name}>")
        if self.state == MIMS.START and name == 'MIMSDB':
            self.state = MIMS.MIMSDB
        elif self.state == MIMS.MIMSDB and name == 'Case':
            self.state = MIMS.CASE
            # self.currentCase['CaseGUID'] = attrs['CaseGUID'].upper()
            self.currentCase['Decedent Name'] = attrs['DeceasedName']
            self.currentCase['Case Number'] = attrs['CaseId']
        elif self.state == MIMS.CASE and name == 'ci_Finance':
            self.state = MIMS.CIFINANCE
        elif self.state == MIMS.CIFINANCE and name == 'row':
            intFin = {}
            # self.fin['FinGUID'] = attrs['FinGUID']
            # self.fin['CaseGUID'] = attrs['CaseGUID']
            if 'DateContract' in attrs:
                try:
                    d = datetime.datetime.strptime(
                        attrs['DateContract'], '%Y-%m-%dT%H:%M:%S.%f')
                except ValueError:
                    d = datetime.datetime.strptime(
                        attrs['DateContract'], '%Y-%m-%dT%H:%M:%S')
                intFin['Contract Date'] = d.strftime('%d/%m/%Y')
            if 'TotalGlobal' in attrs:
                intFin['Global Total'] = "$ {:,.2f}".format(
                    float(attrs['TotalGlobal']))
            if 'Total' in attrs:
                intFin['Sub Total'] = "$ {:,.2f}".format(float(attrs['Total']))
            if 'TotalCashAdvances' in attrs:
                intFin['Cash Advances Total'] = "$ {:,.2f}".format(
                    float(attrs['TotalCashAdvances']))
            if 'TotalAlterations' in attrs:
                intFin['Alterations Total'] = "$ {:,.2f}".format(
                    float(attrs['TotalAlterations']))
            self.finList.append(intFin)
            self.currentCase['Finance'] = self.finList
        elif self.state == MIMS.CASE and name == 'ci_fin_Alterations':
            self.state = MIMS.CIALTERATIONS
        elif self.state == MIMS.CIALTERATIONS and name == 'row':
            intAlt = {}
            # intAlt['FinGUID'] = attrs['FinGUID']
            # intAlt['AltGUID'] = attrs['AltGUID']
            if 'Description' in attrs:
                intAlt['Description'] = attrs['Description']
            if 'Category' in attrs:
                intAlt['Category'] = attrs['Category']
            if 'Price' in attrs:
                intAlt['Price'] = "$ {:,.2f}".format(float(attrs['Price']))
            # if 'Deleted' in attrs:
            #     intAlt['Deleted'] = attrs['Deleted']
            self.altList.append(intAlt)
            # self.alt['Alterations'] = self.altList
            self.currentCase['Alterations'] = self.altList
        elif self.state == MIMS.CASE and name == 'ci_fin_Automotive':
            self.state = MIMS.CIAUTOMOTIVE
        elif self.state == MIMS.CIAUTOMOTIVE and name == 'row':
            intAuto = {}
            # if 'FinGUID' in attrs:
            #     intAuto['FinGUID'] = attrs['FinGUID']
            # if 'AutoGUID' in attrs:
            #     intAuto['AutoGUID'] = attrs['AutoGUID']
            if 'Label' in attrs:
                intAuto['Label'] = attrs['Label']
            if 'Total' in attrs:
                intAuto['Total'] = "$ {:,.2f}".format(float(attrs['Total']))
            # if 'Deleted' in attrs:
            #     intAuto['Deleted'] = attrs['Deleted']
            self.autoList.append(intAuto)
            # self.auto['Automotive'] = self.autoList
            self.currentCase['Automotive'] = self.autoList
        elif self.state == MIMS.CASE and name == 'ci_fin_CashAdvance':
            self.state = MIMS.CICASHADVANCE
        elif self.state == MIMS.CICASHADVANCE and name == 'row':
            intCash = {}
            # if 'FinGUID' in attrs:
            #     intCash['FinGUID'] = attrs['FinGUID']
            # if 'CashAdvGUID' in attrs:
            #     intCash['CashAdvGUID'] = attrs['CashAdvGUID']
            if 'Description' in attrs:
                intCash['Description'] = attrs['Description']
            if 'Total' in attrs:
                intCash['Total'] = "$ {:,.2f}".format(float(attrs['Total']))
            # if 'Deleted' in attrs:
            #     intCash['Deleted'] = attrs['Deleted']
            self.cashList.append(intCash)
            # self.cash['Cash'] = self.cashList
            self.currentCase['Cash'] = self.cashList
        elif self.state == MIMS.CASE and name == 'ci_fin_Facilities':
            self.state = MIMS.CIFACILITIES
        elif self.state == MIMS.CIFACILITIES and name == 'row':
            intFac = {}
            # if 'FinGUID' in attrs:
            #     intFac['FinGUID'] = attrs['FinGUID']
            # if 'FacGUID' in attrs:
            #     intFac['FacGUID'] = attrs['FacGUID']
            if 'Label' in attrs:
                intFac['Label'] = attrs['Label']
            if 'Total' in attrs:
                intFac['Total'] = "$ {:,.2f}".format(float(attrs['Total']))
            # if 'Deleted' in attrs:
            #     intFac['Deleted'] = attrs['Deleted']
            self.facList.append(intFac)
            # self.fac['Facilities'] = self.facList
            self.currentCase['Facilities'] = self.facList
        elif self.state == MIMS.CASE and name == 'ci_fin_Merchandise':
            self.state = MIMS.CIMERCHANDISE
        elif self.state == MIMS.CIMERCHANDISE and name == 'row':
            intMerch = {}
            # if 'FinGUID' in attrs:
            #     intMerch['FinGUID'] = attrs['FinGUID']
            # if 'MerchGUID' in attrs:
            #     intMerch['MerchGUID'] = attrs['MerchGUID']
            if 'Label' in attrs:
                intMerch['Label'] = attrs['Label']
            if 'Supplier' in attrs:
                intMerch['Supplier'] = attrs['Supplier']
            if 'Description1' in attrs and 'Description2' in attrs:
                intMerch['Description'] = attrs['Description1'] + \
                    ' ' + attrs['Description2']
            # if 'Description2' in attrs:
            #     intMerch['Description2'] = attrs['Description2']
            if 'KindOfMetal' in attrs:
                intMerch['Kind Of Metal'] = attrs['KindOfMetal']
            if 'Model' in attrs:
                intMerch['Model'] = attrs['Model']
            if 'Color' in attrs:
                intMerch['Color'] = attrs['Color']
            # if 'Emblem' in attrs:
            #     intMerch['Emblem'] = attrs['Emblem']
            if 'ExteriorColor' in attrs:
                intMerch['Exterior Color'] = attrs['ExteriorColor']
            # if 'Quantity' in attrs:
            #     intMerch['Quantity'] = attrs['Quantity']
            # if 'Cost' in attrs:
            #     intMerch['Cost'] = attrs['Cost']
            if 'Price' in attrs:
                intMerch['Price'] = "$ {:,.2f}".format(float(attrs['Price']))
            # if 'Deleted' in attrs:
            #     intMerch['Deleted'] = attrs['Deleted']
            self.merchList.append(intMerch)
            # self.merch['Merchandise'] = self.merchList
            self.currentCase['Merchandise'] = self.merchList
        else:
            eprint(f"UNHANDLED <{name}> FROM STATE {self.state}")

    def endElement(self, name):
        eprint(f"<<IN STATE: {self.state}\t\tEND ELEMENT: <{name}>")
        if name == 'MIMSDB':
            self.state = MIMS.END
            eprint("All done!")
        elif name == 'Case':
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
            # print(type(_jOut))
            # print(f'json2html prints: {type(json2html.convert(jOut))}')
            if self.currentCase['Case Number'] == '20-006':
                with open('mims_merch1.html', 'w') as o:
                    o.write(headHTML +
                            f"{self.currentCase['Decedent Name']}"
                            + styleHTML + json2html.convert(
                                jOut, clubbing=True, ) + tailHTML)
            self.currentCase = {}
            self.finList = []
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
