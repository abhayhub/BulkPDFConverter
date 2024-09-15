import aspose.words as aw
import os

for filename in os.listdir('./bulkfile'):
    f = os.path.join('./bulkfile',filename)
    if os.path.isfile(f):
        n = len(filename)
        doc = aw.Document(f'./bulkfile/{filename}')
        doc.save(f'./outputfile/{filename[:n-5]}.pdf')