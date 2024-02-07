FROM python:3.12.2-alpine

COPY ./requirements.txt requirements.txt
COPY ./solutions/sixth/sixth.py ./solutions/sixth/sixth.py

RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["python3","-m","solutions.sixth.sixth"]

