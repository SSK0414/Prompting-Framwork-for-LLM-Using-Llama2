# importing required modules
import PyPDF2
 
# creating a pdf file object
pdfFileObj = open(r"D:\PDF\film-review.original.pdf", 'rb')   # over here we will have to get the name of the filefrom the front end that is the webpage and just put it here
 
# creating a pdf reader object
pdfReader = PyPDF2.PdfReader(pdfFileObj)
 
# printing number of pages in pdf file
l = len(pdfReader.pages)
print(l)
p=''
# creating a page object
for i in range(0,l):
    pageObj = pdfReader.pages[i]
    p += pageObj.extract_text()

 
# extracting text from page
print(p)
 
# closing the pdf file object
pdfFileObj.close()
