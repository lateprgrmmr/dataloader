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
    CIDEATHINFO = 5
    END = 1000


class MIMSHandler(xml.sax.ContentHandler):

    def __init__(self):
        self.state = MIMS.START
        self.currentCase = {}
        self.cases = pd.DataFrame(columns=['CaseGUID', 'case_number',
                                           'case_type', 'created_time',
                                           'date_of_birth', 'date_of_death',
                                           'time_of_death', 'assignee.email',
                                           'deathcertificate.about.firstName',
                                           'deathcertificate.about.middleName',
                                           'deathcertificate.about.lastName',
                                           'deathcertificate.about.gender',
                                           'deathcertificate.about.ssn',
                                           'deathcertificate.about.aka'])

    def startElement(self, name, attrs):
        eprint(f">>IN STATE: {self.state}\t\tSTART ELEMENT: <{name}>")
        if self.state == MIMS.START and name == 'MIMSDB':
            self.state = MIMS.MIMSDB
        elif self.state == MIMS.MIMSDB and name == 'Case':
            self.state = MIMS.CASE
            self.currentCase['CaseGUID'] = attrs['CaseGUID']
            self.currentCase['case_number'] = attrs['CaseId']
        elif self.state == MIMS.CASE and name == 'ci_Addresses':
            self.state = MIMS.CIADDRESSES
        elif self.state == MIMS.CIADDRESSES and name == 'row' and attrs['AddressCategory'] == "1":
            self.currentCase['deathcertificate.about.firstName'] = attrs['FirstName']
            self.currentCase['deathcertificate.about.middleName'] = attrs['MiddleName']
            self.currentCase['deathcertificate.about.lastName'] = attrs['LastName']
            self.currentCase['deathcertificate.about.ssn'] = attrs['SSNumber']
            if 'DateOfBirth' in attrs:
                self.currentCase['date_of_birth'] = attrs['DateOfBirth']
            if 'DateOfDeath' in attrs:
                self.currentCase['date_of_death'] = attrs['DateOfDeath']
        elif self.state == MIMS.CASE and name == 'ci_CaseData':
            self.state = MIMS.CICASEDATA
        elif self.state == MIMS.CICASEDATA and name == 'row':
            if 'RegistrationNumDirector' in attrs:
                self.currentCase['assignee.email'] = 'jon@haugheyfuneralhome.com'
            self.currentCase['created_time'] = attrs['Created']
            if 'IsPreneed' in attrs and attrs['IsPreneed'] == "0":
                self.currentCase['case_type'] = 'at-need'
            elif 'IsPreneed' in attrs and attrs['IsPreneed'] == "1":
                self.currentCase['case_type'] = 'pre-need'
            if 'Sex' in attrs and attrs['Sex'] == "0":
                self.currentCase['deathcertificate.about.gender'] = 'Female'
            elif 'Sex' in attrs and attrs['Sex'] == "1":
                self.currentCase['deathcertificate.about.gender'] = 'Male'
            self.currentCase['deathcertificate.about.aka'] = attrs['NickName']
        elif self.state == MIMS.CASE and name == 'ci_DeathInfo':
            self.state = MIMS.CIDEATHINFO
        elif self.state == MIMS.CIDEATHINFO and name == 'row':
            if 'TimeOfDeath' in attrs:
                self.currentCase['time_of_death'] = attrs['TimeOfDeath']
        else:
            eprint(f"UNHANDLED <{name}> FROM STATE {self.state}")

    def endElement(self, name):
        eprint(f"<<IN STATE: {self.state}\t\tEND ELEMENT: <{name}>")
        if name == 'MIMSDB':
            self.state = MIMS.END
            eprint("All done!")
        elif name == 'Case':
            # Do something with the currentCase (other than just print it)
            self.cases = self.cases.append(self.currentCase, ignore_index=True)
            self.cases.to_csv('CaseOut.csv')
            self.currentCase = {}
            self.state = MIMS.MIMSDB
        elif name == 'ci_Addresses':
            self.state = MIMS.CASE
        elif name == 'ci_CaseData':
            self.state = MIMS.CASE
        elif name == 'ci_DeathInfo':
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
