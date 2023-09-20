# importing required modules
from PyPDF2 import PdfReader

# creating a pdf reader object
reader = PdfReader('my.pdf')


# printing number of pages in pdf file
print(len(reader.pages))

text=""

for i in range(len(reader.pages)):
    page = reader.pages[i]
    text += page.extract_text()

print(text)



from googletrans import Translator
translator = Translator()
result = translator.translate(text,dest="hi")
print(result.text)