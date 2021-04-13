import xml.sax
# import xml.etree.ElementTree as ET


class CaseHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ''
        self.caseId = ''
        self.decedent = ''
        self.DOD = ''
        # self.address = 'ci_Addresses'
        # self.death = 'ci_DeathInfo'
        # self.survivor = 'ci_Survivors'
        self.count = 0
        # self.deceased = 'DeceasedName'

    def startElement(self, tagName, attrs):
        self.CurrentData = tagName
        if tagName == 'Case':
            self.count += 1
            # caseId = attrs['CaseId']
            # decedent = attrs['DeceasedName']
            # DOD = attrs['DOD']
            # print(f'Case: {caseId} Deceased: {decedent} DateOfDeath: {DOD}')

    # def endElement(self, tagName):
        # if self.CurrentData == 'Case':
        # print(f'Count Cases: {self.count}')

    def characters(self, content):
        if self.CurrentData == 'Case':
            self.caseId += content


def main():
    handler = CaseHandler()

    xml.sax.parse('/Users/kevinbratt/haughey.xml', handler)

    print(f'{handler.count} cases in total')


if __name__ == '__main__':
    main()
