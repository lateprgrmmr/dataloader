import pdfreader
from pdfreader import PDFDocument, SimplePDFViewer

fd = open('nomis_sample.pdf', 'rb')
doc = PDFDocument(fd)
#viewer = SimplePDFViewer(fd)
# viewer.navigate()
# print(viewer.render())

# print(doc.header.version)
# print(doc.root.Type)
# print(doc.root.Metadata.Subtype)
# print(doc.root.Outlines.First['Title'])
print(pdfreader.types.objects.Page(doc))

U = v.canvas.strings
for each in U:
    u = each.replace('.', '').replace('\n', '').replace('\b', '')
    print(''.join(u))
