from flask import Flask, render_template, request
import resume_funct as rf
app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def home():
    return render_template('home.html')

@app.route('/resumes_name', methods = ['GET','POST'])
def resumes_name():
    if request.method == "POST":
        names = []
        pdf_files = request.files.getlist("files")
        for pdf_file in pdf_files:
            text = rf.text_from_pdf(pdf_file)
            name = rf.extract_name(text)
            names.append(name)
        return render_template('home.html', names = names)
    render_template('home.html')

if __name__ == "__main__":
    app.run(debug = True)