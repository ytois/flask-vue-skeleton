FROM python:3.6-alpine

ARG work_dir=/var/www
RUN mkdir $work_dir
WORKDIR $work_dir

RUN apk add --no-cache vim
RUN apk add --no-cache uwsgi-python3

# install python lib
RUN pip3 install pipenv
COPY Pipfile $work_dir
RUN pipenv install --system --skip-lock

# CMD ["python3", "/var/www/backend/manage.py", "runserver", "-h", "0.0.0.0", "-p", "5000"]
CMD ["uwsgi", "--ini", "backend/uwsgi.ini"]
