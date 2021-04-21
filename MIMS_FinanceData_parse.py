import xml.sax
from enum import Enum
import json
import jinja2

import datetime
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

    def startElement(self, name, attrs):
        eprint(f">>IN STATE: {self.state}\t\tSTART ELEMENT: <{name}>")
        if self.state == MIMS.START and name == 'MIMSDB':
            self.state = MIMS.MIMSDB
        elif self.state == MIMS.MIMSDB and name == 'Case':
            self.state = MIMS.CASE
            self.currentCase['Decedent Name'] = attrs['DeceasedName']
            self.currentCase['Case Number'] = attrs['CaseId']
        elif self.state == MIMS.CASE and name == 'ci_Finance':
            self.state = MIMS.CIFINANCE
        elif self.state == MIMS.CIFINANCE and name == 'row':
            intFin = {}
            if 'DateContract' in attrs:
                try:
                    d = datetime.datetime.strptime(
                        attrs['DateContract'], '%Y-%m-%dT%H:%M:%S.%f')
                except ValueError:
                    d = datetime.datetime.strptime(
                        attrs['DateContract'], '%Y-%m-%dT%H:%M:%S')
                intFin['Contract Date'] = d.strftime('%m/%d/%Y')
            if 'CreditDescription' in attrs or 'Credit2Description' in attrs:
                intFin['Credit Descriptions'] = (attrs['CreditDescription'] + ' ' +
                                                 attrs['Credit2Description']).strip()
            if 'Credit' in attrs:
                intCredit = 0
                intCredit += (float(attrs['Credit']) +
                              float(attrs['Credit2']) + float(attrs['Credit3']))
                intFin['Total Credits'] = intCredit
            if 'Total' in attrs:
                intFin['Sub Total'] = round(float(attrs['Total']), 2)
            if 'TotalGlobal' in attrs:
                intFin['Global Total'] = "$ {:,.2f}".format(
                    float(attrs['TotalGlobal']))
            # self.finList.append(intFin)
            # self.fin = self.finList
            self.currentCase['Finance'] = intFin
        elif self.state == MIMS.CASE and name == 'ci_fin_Alterations':
            self.state = MIMS.CIALTERATIONS
        elif self.state == MIMS.CIALTERATIONS and name == 'row':
            intAlt = {}
            if 'Description' in attrs:
                intAlt['Description'] = attrs['Description']
            if 'Price' in attrs:
                intAlt['Total'] = round(float(attrs['Price']), 2)
            # if 'Deleted' in attrs:
            #     intAlt['Deleted'] = attrs['Deleted']
            self.altList.append(intAlt)
            # self.alt['Alterations'] = self.altList
            self.currentCase['Alterations'] = self.altList
        elif self.state == MIMS.CASE and name == 'ci_fin_Automotive':
            self.state = MIMS.CIAUTOMOTIVE
        elif self.state == MIMS.CIAUTOMOTIVE and name == 'row':
            intAuto = {}
            if 'Label' in attrs:
                intAuto['Description'] = attrs['Label']
            if attrs['Label'] == 'Transfer Remains:':
                intAuto['Total'] = 470.00
            elif 'Price' in attrs:
                intAuto['Total'] = round(float(attrs['Price']), 2)
            # if 'Deleted' in attrs:
            #     intAuto['Deleted'] = attrs['Deleted']
            self.autoList.append(intAuto)
            # self.auto['Automotive'] = self.autoList
            self.currentCase['Automotive'] = self.autoList
        elif self.state == MIMS.CASE and name == 'ci_fin_CashAdvance':
            self.state = MIMS.CICASHADVANCE
        elif self.state == MIMS.CICASHADVANCE and name == 'row':
            intCash = {}
            if 'Description' in attrs:
                intCash['Description'] = attrs['Description']
            if 'Total' in attrs:
                intCash['Total'] = round(float(attrs['Total']), 2)
            # if 'Deleted' in attrs:
            #     intCash['Deleted'] = attrs['Deleted']
            self.cashList.append(intCash)
            # self.cash['Cash'] = self.cashList
            self.currentCase['Cash'] = self.cashList
        elif self.state == MIMS.CASE and name == 'ci_fin_Facilities':
            self.state = MIMS.CIFACILITIES
        elif self.state == MIMS.CIFACILITIES and name == 'row':
            intFac = {}
            if 'Label' in attrs:
                intFac['Description'] = attrs['Label']
            if 'Total' in attrs:
                intFac['Total'] = round(float(attrs['Total']), 2)
            # if 'Deleted' in attrs:
            #     intFac['Deleted'] = attrs['Deleted']
            self.facList.append(intFac)
            # self.fac['Facilities'] = self.facList
            self.currentCase['Facilities'] = self.facList
        elif self.state == MIMS.CASE and name == 'ci_fin_Merchandise':
            self.state = MIMS.CIMERCHANDISE
        elif self.state == MIMS.CIMERCHANDISE and name == 'row':
            intMerch = {}
            if 'Description1' in attrs and 'Description2' in attrs:
                intMerch['Description'] = (attrs['Label'] + ' ' +
                                           attrs['Supplier'] + ' ' +
                                           attrs['Description1'] + ' ' +
                                           attrs['Description2'] + ' ' +
                                           attrs['KindOfMetal'] + ' ' +
                                           attrs['Model'] + ' ' +
                                           attrs['Color'] + ' ' +
                                           attrs['Emblem'] + ' ' +
                                           attrs['ExteriorColor']).strip()
            if 'Price' in attrs:
                intMerch['Total'] = round(float(attrs['Price']), 2)
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
            try:
                altTotal = self.currentCase['Alterations']
                altTtl = []
                for alt in altTotal:
                    try:
                        altTtl.append(alt['Total'])
                    except KeyError:
                        altTtl.append(0.00)
                self.currentCase['Finance']['Total Alterations'] = sum(altTtl)
            except KeyError:
                pass
            try:
                autoTotal = self.currentCase['Automotive']
                autoTtl = []
                for auto in autoTotal:
                    try:
                        autoTtl.append(auto['Total'])
                    except KeyError:
                        autoTtl.append(0.00)
                self.currentCase['Finance']['Total Automotive'] = sum(autoTtl)
            except KeyError:
                pass
            try:
                cashTotal = self.currentCase['Cash']
                cashTtl = []
                for cash in cashTotal:
                    try:
                        cashTtl.append(cash['Total'])
                    except KeyError:
                        cashTtl.append(0.00)
                self.currentCase['Finance']['Total Cash Advances'] = sum(
                    cashTtl)
            except KeyError:
                pass
            try:
                facTotal = self.currentCase['Facilities']
                facTtl = []
                for fac in facTotal:
                    try:
                        facTtl.append(fac['Total'])
                    except KeyError:
                        facTtl.append(0.00)
                self.currentCase['Finance']['Total Facility'] = sum(facTtl)
            except KeyError:
                pass
            try:
                merchTotal = self.currentCase['Merchandise']
                merchTtl = []
                for merch in merchTotal:
                    try:
                        merchTtl.append(merch['Total'])
                    except KeyError:
                        merchTtl.append(0.00)
                self.currentCase['Finance']['Total Merchandise'] = sum(
                    merchTtl)
            except KeyError:
                pass
            # if self.currentCase['Case Number'] == '21-24':
            jOut = json.dumps(self.currentCase)
            jUse = json.loads(jOut)
            with open('case_data.json', 'w') as f:
                f.write(json.dumps(self.currentCase))

            templateLoader = jinja2.FileSystemLoader(searchpath='./')
            templateEnv = jinja2.Environment(loader=templateLoader)
            TEMPLATE_FILE = 'pdf_temp.html'
            template = templateEnv.get_template(TEMPLATE_FILE)

            for e in jUse:
                output = template.render(case=jUse)
                html_file = open('mims_finance.html', 'w')
                html_file.write(output)
                html_file.close()
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
