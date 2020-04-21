FROM python:3.8-slim-buster

WORKDIR /usr/src/inserter
RUN pip install psycopg2-binary essential-generators
ADD main.py .

CMD ["python", "main.py"]
