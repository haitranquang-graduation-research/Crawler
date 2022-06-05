FROM python:3.8.10

RUN pip install selenium

COPY . .

CMD ["python","generic_crawler.py"]