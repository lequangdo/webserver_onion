# start from an official image
FROM python:3.6

# arbitrary location choice: you can change the directory
RUN mkdir -p /home/ubuntu/server
WORKDIR /home/ubuntu/server

# install our two dependencies
RUN pip install django gunicorn psycopg2-binary
RUN pip install requests

# copy our project code
COPY . /home/ubuntu/server
