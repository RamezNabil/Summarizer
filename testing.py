import PyPDF2
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM,  T5Tokenizer, T5ForConditionalGeneration, T5Config

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

def Summarize(document):
    model = T5ForConditionalGeneration.from_pretrained('t5-small')
    tokenizer = T5Tokenizer.from_pretrained('t5-small')
    device = torch.device('cpu')
    preprocess_text = document.strip().replace("\n", " ")
    t5_prepared_Text = "summarize: " + preprocess_text
    tokenized_text = tokenizer.encode(t5_prepared_Text, return_tensors="pt", max_length=600, truncation=True).to(device)
    summary_ids = model.generate(tokenized_text,
                                 num_beams=2,
                                 no_repeat_ngram_size=2,
                                 min_length=10,
                                 max_length=100,
                                 early_stopping=False)

    output = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return output

def Summarize2(document):
    tokenizer = AutoTokenizer.from_pretrained("t5-base")
    model = AutoModelForSeq2SeqLM.from_pretrained("t5-base", return_dict=True)
    inputs = tokenizer.encode("summarize: " + document, return_tensors='pt', max_length=600, truncation=True)
    outputs = model.generate(inputs, max_length=100, min_length=10, length_penalty=5, num_beams=2)
    summary = tokenizer.decode(outputs[0])
    return summary

def Output(document):
    for x in document.split('.'):
        x = x.replace('<pad>', "")
        x = x.replace('</s>', "")
        x = x.strip()
        if x != "":
            print(x + '.')

pdf = ReadingFromPDF("Assignment.pdf",1,7)
preprocess_text = pdf.strip().replace("\n","")
t5_prepared_Text = "summarize: "+preprocess_text
pdf = t5_prepared_Text

# pdf = ("""
# The US has "passed the peak" on new coronavirus cases, President Donald Trump said and predicted that some states would reopen this month.
#
# The US has over 637,000 confirmed Covid-19 cases and over 30,826 deaths, the highest for any country in the world.
#
# At the daily White House coronavirus briefing on Wednesday, Trump said new guidelines to reopen the country would be announced on Thursday after he speaks to governors.
#
# "We'll be the comeback kids, all of us," he said. "We want to get our country back."
#
# The Trump administration has previously fixed May 1 as a possible date to reopen the world's largest economy, but the president said some states may be able to return to normalcy earlier than that.
# """)

# Output
print(pdf)
print("\nSummary 1:")
Output(Summarize(pdf))
print("\nSummary 2:")
Output(Summarize2(pdf))

