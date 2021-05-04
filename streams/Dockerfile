FROM ubuntu
RUN apt-get update
RUN apt-get install -y python3-pip
RUN apt-get install -y vim
RUN pip3 install redis
RUN mkdir -p /data/scripts
COPY . /data/scripts
WORKDIR /data/scripts
