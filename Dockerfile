FROM python:3.8.10-slim-buster
RUN mkdir /crawler
WORKDIR /crawler
COPY ./requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .
CMD ["python","generic_crawler.py"]

EXPOSE 5200