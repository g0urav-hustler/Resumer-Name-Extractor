import pytesseract
from pdf2image import text_from_path
import os
import re

def text_from_pdf(resume_obj):
    images = text_from_path(resume_obj)
    text = pytesseract.image_to_string(images[0])
    return text

def extract_name(text):
    text = text.split("\n")
    name = text[0]
    if len(text[0].split(' ')) < 2:
        name = name + ' ' + text[1]
    return name

if __name__ == "__main__":
    resumes_path = str(input("Enter resumes folder path: "))
    resumes_list = os.listdir(resumes_path)
    for resume in resumes_list:
        resume_path = resumes_path + '/' + resume
        open_resume = open(resume_path, 'rb')
        text = text_from_pdf(open_resume)
        open_resume.close()
        name = extract_name(text)
        print(resume,'=> ' , name)
    