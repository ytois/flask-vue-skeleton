FROM alpine
# FROM python:3.6-alpine

ARG work_dir=/var/www
RUN mkdir $work_dir
WORKDIR $work_dir

RUN apk add --no-cache \
    python3 \
    vim \
    uwsgi \
    uwsgi-python3 && \
    python3 -m ensurepip

# install python lib
COPY Pipfile $work_dir
RUN pip3 install pipenv && \
    pipenv install --system --skip-lock

CMD ["uwsgi", "--ini", "backend/uwsgi.ini"]
