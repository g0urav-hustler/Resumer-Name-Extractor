
<h1 align="center" >Electronic Component Scanner</h1>

**Website** : [Resumer Name Extractor](https://resumer-name-extractor.herokuapp.com/)


## Overview
#### It was a website that extract candidates name and make a excel file of candidates names and their file name. Than the excel file can be downloaded in the local computer. 
### Web view:
![](https://github.com/g0urav-hustler/Resumer-Name-Extractor/blob/master/web%20image/website%20image.png)

----------------------------
## Technical Aspects
- Extract the text frm pdf page.
- Extract the proper name of the person from the text

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
$ docker build -t [app-name]:latest .
 ```
To run the docker container
``` 
$ docker run -p80:8000 [app-name]
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


----------------------------
## Repository Overview
```
├── __pycache__
├── static 
│   └──syle.css
├── templates
│   └── home.html
├── Dockerfile
├── README.md
├── app.py
├── requirements.txt
└── resume_funct.py
```


