import PyPDF2

def ReadingFromPDF(filename,f,l):
    pdfFile = open(filename, "rb")
    pdfReader = PyPDF2.PdfFileReader(pdfFile)
    numOfPages = pdfReader.numPages
    pdf = ""
    for i in range(f-1,l):
        page = pdfReader.getPage(i)
        pdf += page.extractText()

    return pdf
    pdfFile.close()

    pdf = ReadingFromPDF("Assignment.pdf",1,7)
    preprocess_text = pdf.strip().replace("\n","")
    t5_prepared_Text = "summarize: "+preprocess_text
    pdf = t5_prepared_Text
    return pdf