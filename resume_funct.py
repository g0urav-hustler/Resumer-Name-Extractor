from io import StringIO
import spacy
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
import os

def extract_name(input_string):
    nlp = spacy.load('en_core_web_sm')
    input_string = str(input_string)
    doc = nlp(input_string)
    # Extract entities
    doc_entities = doc.ents

    # Subset to person type entities
    doc_persons = filter(lambda x: x.label_ == 'PERSON', doc_entities)
    doc_persons = filter(lambda x: len(x.text.strip().split()) >= 2, doc_persons)
    doc_persons = list(map(lambda x: x.text.strip(), doc_persons))
    
    if(len(doc_persons) == 0):
        return doc_persons
    # Assuming that the first Person entity with more than two tokens is the candidate's name
    candidate_name = doc_persons[0]
    return candidate_name


def text_from_pdf(pdf_path):
    output_string = StringIO()
    with open(pdf_path, 'rb') as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)
    device.close()
    text = output_string.getvalue()
    output_string.close()
    return text


if __name__ == "__main__":
    resumes_path = str(input("Enter resumes folder path: "))
    resumes_list = os.listdir(resumes_path)
    for resume in resumes_list:
        resume_path = resumes_path + '/' + resume
        text = text_from_pdf(resume_path)
        name = extract_name(text)
        print(resume,'=> ' , name)
    