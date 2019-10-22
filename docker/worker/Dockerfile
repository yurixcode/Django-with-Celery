FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /worker
WORKDIR /worker
COPY requirements/worker/requirements.txt /worker/
COPY scripts/run_celery.sh /worker/

RUN pip install -r requirements.txt

COPY . /worker/