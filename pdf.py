import pdfreader
from pdfreader import PDFDocument, SimplePDFViewer

fd = open('nomis_sample.pdf', 'rb')
doc = PDFDocument(fd)
viewer = SimplePDFViewer(fd)
#viewer.navigate()
# print(viewer.render())
print(viewer.render())
# print(doc.header.version)
# print(doc.root.Type)
# print(doc.root.Metadata.Subtype)
# print(doc.root.Outlines.First['Title'])
