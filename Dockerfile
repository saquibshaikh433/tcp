# base image from docker hub
FROM python:3.8
# copy all the local code and repo to new docker folder
COPY . /tcp-app
#change working directory to docker folder 
WORKDIR /tcp-app
# install all the requirements 
RUN pip install -r requirements.txt
# expose new port to 
EXPOSE $PORT
# gunicorn split task into instance and allow work load accordingly
CMD gunicorn -w 4 -b 0.0.0.0:$PORT app:app