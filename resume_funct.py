from io import StringIO
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
import os
import re
import time

def text_from_pdf(file_obj):
    output_string = StringIO()
    parser = PDFParser(file_obj)
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

def extract_name(text):
    name = ''
    text = text.split("\n")
    re_pattern = '[A-za-z]+\s[A-za-z]+'
    for i in range(len(text)):
        if "Name" in text[i] or "NAME":
            text[i] = re.sub("Name", '', text[i])
            text[i] = re.sub("NAME", '', text[i])
        if "Resume" in text[i] or "RESUME" in text[i]:
            text[i] = re.sub("Resume", '', text[i])
            text[i] = re.sub("RESUME", '', text[i])
        
        if re.findall(re_pattern, text[i]) != []:
            name = re.findall(re_pattern, text[i])[0]
            break
        else:
            if re.findall('[A-Za-z]+', text[i]) != []:
                first = re.findall('[A-Za-z]+', text[i])[0]
                if (re.findall('[^A-Za-z ]', text[i+1]) == []) and (re.findall('[A-Za-z]+', text[i+1]) != []):
                    second = re.findall('[A-Za-z]+', text[i+1])[0]
                    name = first + ' ' + second
                    break
                name = first
                break
            else:
                continue
    
    name = name.split(' ')
    for i in range(len(name)):
        name[i] = name[i].capitalize()
    name = " ".join(name)
    return name

if __name__ == "__main__":
    resumes_path = str(input("Enter resumes folder path: "))
    resumes_list = os.listdir(resumes_path)
    start = time.time()
    for resume in resumes_list:
        resume_path = resumes_path + '/' + resume
        file_obj = open(resume_path, 'rb')
        text = text_from_pdf(file_ob)
        name = extract_name(text)
        file_obj.close()
        print(resume,'==> ' , name)
    end =time.time()
    print("Total Time = ", (end-start)/60)
