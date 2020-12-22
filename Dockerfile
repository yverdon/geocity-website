FROM debian:buster-slim

WORKDIR /app

RUN apt-get update \
  && apt-get -y install build-essential pkg-config nano curl wget unzip \
  && apt-get -y install sqlite3 libsqlite3-dev libtiff5 libtiff5-dev libcurl4-openssl-dev libhdf5-dev \
  && apt-get -y autoremove --purge && apt-get -y autoclean

