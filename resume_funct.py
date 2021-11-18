import pytesseract
from pdf2image import convert_from_bytes
import os
import re
import time

def text_from_pdf(resume):
    dpi = 800
    images = convert_from_bytes(resume.read())
    text = pytesseract.image_to_string(images[0])
    return text

def extract_name(text):
    name = ''
    text = text.split("\n")
    re_pattern = '[A-za-z]+\s[A-za-z]+'
    for i in range(10):
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
        text = text_from_pdf(resume_path)
        name = extract_name(text)
        print(resume,'==> ' , name)
    end =time.time()
    print("Total Time = ", (end-start)/60)
