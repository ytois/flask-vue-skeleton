FROM python:3.6-alpine


ARG work_dir=/var/www
RUN mkdir $work_dir
WORKDIR $work_dir

RUN apk add --no-cache vim
RUN pip install pipenv

COPY Pipfile $work_dir

RUN pipenv install --system --skip-lock

CMD ["python3", "/var/www/backend/manage.py", "runserver", "-h", "0.0.0.0", "-p", "5000"]