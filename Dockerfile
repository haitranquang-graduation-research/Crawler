FROM python:3.8.10-slim-buster
RUN mkdir /crawler
WORKDIR /crawler
COPY ./requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .
CMD ["flask","run","--host=0.0.0.0","--port=5200"]

EXPOSE 5200