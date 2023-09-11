#########
# FINAL #
#########

# pull official base image
FROM python:3

# create directory for the app user
RUN mkdir -p /home/app

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfile
WORKDIR $APP_HOME

# install dependencies
COPY requirements.txt $APP_HOME

RUN pip install -r requirements.txt

# copy project
COPY . $APP_HOME

