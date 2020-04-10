ARG PYTHON_VERSION=3.7.4

FROM python:$PYTHON_VERSION-slim-buster

RUN apt-get update -qq \
  && DEBIAN_FRONTEND=noninteractive apt-get install -yq \
    libpq-dev \
    gcc

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 5000

CMD python app.py
