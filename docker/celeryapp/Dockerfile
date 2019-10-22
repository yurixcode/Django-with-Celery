FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY requirements/celeryapp/requirements.txt /app/
COPY scripts/start.sh /app/

RUN pip install -r requirements.txt

COPY . /app/
