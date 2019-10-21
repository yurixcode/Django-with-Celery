FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /worker
WORKDIR /worker
COPY requirements.txt /worker/
COPY run_celery.sh /worker/

RUN pip install -r requirements.txt

COPY . /worker/

# CMD pm2 start redis_server