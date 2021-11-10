FROM python:3.8-slim-buster

RUN pip install rq-dashboard>=0.6.1
RUN pip install click>=7.1.2

EXPOSE 9181

CMD ["rq-dashboard"]
