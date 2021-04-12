import PyPDF2


def ReadingFromPDF(filename, f, l):
    pdfFile = open(filename, "rb")
    pdfReader = PyPDF2.PdfFileReader(pdfFile)
    numOfPages = pdfReader.numPages
    pdf = ""
    for i in range(f - 1, l):
        page = pdfReader.getPage(i)
        pdf += page.extractText()

    pdfFile.close()


    return pdf