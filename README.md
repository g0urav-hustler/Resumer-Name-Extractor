
<h1 align="center" >Resumer Name Extractor</h1>

**Website** : [Resumer Name Extractor](https://resumer-name-extractor.onrender.com)


## Overview
#### It was a website that extract candidates name and make a excel file of candidates names and their file name. Than the excel file can be downloaded in the local computer. 
### Web view:
![](https://github.com/g0urav-hustler/Resumer-Name-Extractor/blob/master/readme%20resources/website%20image.png)

----------------------------
## Problem Statement

If a person's job is to hire candidates for your company and you see a lots of resume been submitted for that. Sometimes the files which has been submitted not had an appropriate naming ,so you are confused about whose resume file that has been.

----------------------------
## Goal
To make a python model that takes resume file and extract their name from it,  so that the person easily find out the candidates resume file.

----------------------------
## Technical Aspects
- Extract the text frm pdf page.
- Extract the proper name of the person from the text.
- It can extract about 90%-95% correct names from the resumes.

### Technology Used 
![](https://img.shields.io/badge/Python-3.7-blue.svg)
![](https://img.shields.io/badge/Flask-1.1.1-blue.svg)
![](https://img.shields.io/badge/Docker-20.10.12-blue.svg)
![](https://img.shields.io/badge/Heroku-7.59.1-blue.svg)

----------------------------
## Setup

Open your terminal and change the directory to project folder
```
$ cd [your-project-folder]
```
Clone the repo in your exiting project folder
```
$ git clone https://github.com/g0urav-hustler/Resumer-Name-Extractor.git
```
Making virual environment 
```
$ python3 -m [your-virtual-env-name] [project-directory-path]
```
Activate virtual environment 
```
$ source [your-virtual-env-name]/bin/activate
```
Install all the requirements
```
$ pip install -r requirements.txt
```
Now your setup has been completed to run the app.

----------------------------
## Run App
To Run the app in your local computer
```
$ python app.py
```
----------------------------
## Dockerization
Pre-requisite: Docker Installed in your Computer 

To install Docker, see [Reference](https://runnable.com/docker/getting-started/)

Docker command to build the docker container
```
$ docker build -t [your-app-name]:latest .
 ```
To run the docker container
``` 
$ docker run -p80:8000 [your-app-name]
```
To see docker container 
```
$ docker images
```

----------------------------
## Deployment
The app was deployed on heroku platform.

Pre-requisite : Profile on Heroku and Heroku was install in your computor,

To install Heroku see [Reference](https://devcenter.heroku.com/articles/heroku-cli)

Login to your heroku account
```
$ heroku container:login
```
Create a web app on heroku
```
$ heroku create [your-app-name]
```
Tag your docker container as heroku web app
```
$ docker tag [your-app-name]:latest registry.heroku.com/[your-app-name]/web
```
Pushing the docker container on the web
```
$ docker push registry.heroku.com/[your-app-name]/web
```
Releasing the web app
```
$ heroku container:release web -a [your-app-name]
```

----------------------------
## Repository Overview
```
├── __pycache__
├── readme resources
├── static 
│   └──syle.css
├── templates
│   └── home.html
├── Dockerfile
├── LICENSE
├── README.md
├── app.py
├── requirements.txt
└── resume_funct.py
```

----------------------------
## LICENSE
Copyright(c) 2021 Gourav Chouhan

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

----------------------------
## Team
<img src = "https://github.com/g0urav-hustler/Resumer-Name-Extractor/blob/master/readme%20resources/Profile.png" width = 100> |
-|
[Gourav Chouhan](https://github.com/g0urav-hustler) |


<img src = "readme resources/Sakshi Profile.jpeg" width = 100> |
-|
[Sakshi Jain](https://github.com/sakshi4235) | 

----------------------------

### If you like this repo and it is useful, please don't forget to give a ⭐.


