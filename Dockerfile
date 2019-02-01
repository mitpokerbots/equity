FROM python:2.7-jessie

RUN useradd -ms /bin/bash web

# copy only the files needed for pip install
COPY requirements.txt /home/web/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /home/web/requirements.txt

ENV DEBIAN_FRONTEND noninteractive

RUN echo 'deb http://ftp.debian.org/debian jessie-backports main' >> /etc/apt/sources.list.d/sources.list
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -yq libpoker-eval libpoker-eval-dev libc6-dev

COPY ./deps/pbots_calc/libpbots_calc.so /usr/lib/libpbots_calc.so
COPY ./deps/pbots_calc/pbots_calc.h /usr/include/pbots_calc.h

USER web

# copy the rest of the app
COPY . /home/web

WORKDIR /home/web
