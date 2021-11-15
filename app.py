from flask import Flask, render_template, request
import pandas as pd
import resume_funct as rf
app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def home():
    return render_template('home.html')

@app.route('/resumes_name', methods = ['GET','POST'])
def resumes_name():
    up_files = '0'
    if request.method == "POST":
        up_files = '1'
        person_names = []
        file_names = []
        pdf_files = request.files.getlist("files")
        for pdf_file in pdf_files:
            text = rf.text_from_pdf(pdf_file)
            name = rf.extract_name(text)
            person_names.append(name)
            file_names.append(pdf_file.filename)
        # data_dict = {'Person': person_names, 'Pdf Files': file_names}
        # data_file = pd.DataFrame(data_dict)
        # data_file.to_csv("resume_files.csv", index= False)
        return render_template('home.html', up_files = up_files , persons_file = zip(person_names,file_names))
    render_template('home.html')

if __name__ == "__main__":
    app.run(debug = True)