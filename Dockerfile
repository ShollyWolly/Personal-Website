#Python image
FROM python:latest

#Main location insider docker
WORKDIR /app

#Current Folder
ADD . /app/

#install all the packages
RUN pip3 install -r requirements.txt

#run uWSGI
CMD [ "uwsgi", "app.ini" ]

