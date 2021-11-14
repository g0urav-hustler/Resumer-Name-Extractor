from flask import Flask, render_template, request
import resume_funct as rf
app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def home():
    return render_template('home.html')

@app.route('/resumes_name', methods = ['GET','POST'])
def resumes_name():
    if request.method == "POST":
        file_name = request.files['file_name']
        text = rf.text_from_pdf(file_name)
        name = rf.extract_name(text)
        return render_template('home.html', name = name)
    render_template('home.html')

if __name__ == "__main__":
    app.run(debug = True)