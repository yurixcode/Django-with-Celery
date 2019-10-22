FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /worker
WORKDIR /worker
COPY requirements/worker/requirements.txt /worker/
COPY scripts/run_celery.sh /worker/

RUN pip install -r requirements.txt

RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get install -y nodejs
RUN npm install pm2 -g

COPY . /worker/

CMD pm2-runtime ecosystem.config.js