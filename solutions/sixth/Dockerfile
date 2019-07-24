FROM python:3.7.3-alpine

COPY ./requirements.txt requirements.txt
COPY ./6_sixth/sixth.py ./6_sixth/sixth.py

RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["python3","-m","6_sixth.sixth"]

