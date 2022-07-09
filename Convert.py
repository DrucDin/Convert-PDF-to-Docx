import PyPDF2
a = os.listdir('Pdf')

for i in a:

       with open(a, mode='rb') as f:

             reader = PyPDF2.PdfFileReader(f)

             page = reader.getPage(0)

             print(page.extractText())