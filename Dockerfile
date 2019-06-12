FROM python:2.7-alpine
COPY . /app
WORKDIR /app
RUN mkdir -p /var/www/html/data/
RUN pip install -r requirements.txt
CMD python ./cron.py