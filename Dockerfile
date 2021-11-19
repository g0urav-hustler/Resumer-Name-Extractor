FROM continuumio/anaconda3:2020.11
WORKDIR /app 
COPY . .
RUN pip install -r requirements.txt
CMD [ "python", "app.py" ]