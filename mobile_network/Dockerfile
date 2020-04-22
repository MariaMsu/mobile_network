FROM python:3.7-stretch

WORKDIR workdir
COPY ./ ./

RUN pip install -e .

ENV HOST 0.0.0.0
ENV PORT 5019

CMD run_server -hs $HOST -p $PORT