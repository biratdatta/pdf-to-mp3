import pyttsx3
from PyPDF2 import PdfReader
# importing the fileg
book = open('/home/tarib/Desktop/pdftomp3/2020-LIONS-CLUB-CODE-OF-CONDUCT.pdf', 'rb')
pdfReader = PdfReader(book)
pages = len(pdfReader.pages)
print(pages)

speaker = pyttsx3.init()
for num in range(pages):
    page = pdfReader.pages[num]
    text = page.extract_text()
    speaker.say(text)
    speaker.runAndWait()

    #  (Ctrl+C) to stop the Audio
    if speaker._driver.status().state == pyttsx3.engine.EngineState.INTERRUPTED:
        break

book.close()
