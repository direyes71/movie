FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
COPY . /code/
RUN cd /code/ && pip install -r requirements.txt
WORKDIR /code/