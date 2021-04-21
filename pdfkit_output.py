import pdfkit

options = {
    'page-size': 'Letter',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    'quiet': ''
}
pdfkit.from_file('mims_finance.html',
                 'mimsPDFTest.pdf', options=options)
