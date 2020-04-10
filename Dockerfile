ARG PYTHON_VERSION=3.7.6
# ARG PG_MAJOR=11

FROM python:$PYTHON_VERSION-slim-buster

RUN apt-get update -qq \
  && DEBIAN_FRONTEND=noninteractive apt-get install -yq \
    libpq-dev \
    gcc
#     gnupg2 \
#     curl \
#   && apt-get clean \
#   && rm -rf /var/cache/apt/archives/* \
#   && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
#   && truncate -s 0 /var/log/*log

# RUN curl -sSL https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - \
#   && echo 'deb http://apt.postgresql.org/pub/repos/apt/ buster-pgdg main' $PG_MAJOR > /etc/apt/sources.list.d/pgdg.list

# RUN apt-get update -qq && DEBIAN_FRONTEND=noninteractive apt-get -yq dist-upgrade && \
#   DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends \
#     postgresql-client-$PG_MAJOR

WORKDIR /app

COPY . /app

# RUN bash

RUN pip install -r requirements.txt

EXPOSE 5000

CMD python app.py
