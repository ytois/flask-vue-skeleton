FROM alpine

ARG work_dir=/var/www
RUN mkdir $work_dir
WORKDIR $work_dir

RUN apk add --no-cache \
    vim \
    python3-dev \
    uwsgi \
    uwsgi-python3 \
    && python3 -m ensurepip \
    && pip3 install --upgrade pip setuptools

# for psycopg2
RUN apk add --no-cache \
    gcc \
    musl-dev \
    postgresql-dev

# install python lib
COPY Pipfile $work_dir
RUN pip3 install pipenv && \
    pipenv install --system --skip-lock

CMD ["uwsgi", "--ini", "backend/uwsgi.ini"]
