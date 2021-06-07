#FROM jazzdd/alpine-flask:python3.7
FROM python:3.7-alpine

ARG BUILD_DATE
ARG VCS_REF

RUN pip install --upgrade pip

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 7373

CMD [ "python", "servidor.py" ]