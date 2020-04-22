FROM python:3.7-stretch

WORKDIR workdir
COPY ./ ./

ENV HOST 0.0.0.0
ENV PORT 5019

CMD python client.py -hs $HOST -p $PORT
