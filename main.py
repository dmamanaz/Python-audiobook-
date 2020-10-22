import pyttsx3
import PyPDF2

book = open('The Phoenix Project _ A Novel about IT, DevOps, and Helping Your Business Win ( PDFDrive ).pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)

speaker = pyttsx3.init()
for num in range(15, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()