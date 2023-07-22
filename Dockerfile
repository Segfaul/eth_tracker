FROM python:3.11

RUN mkdir /eth_tracker

WORKDIR /eth_tracker

COPY . .

RUN pip install -r requirements.txt