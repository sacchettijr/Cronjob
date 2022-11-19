FROM ubuntu:22.04
RUN apt-get update
RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update
RUN apt-get install -y python3
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN apt-get install -y python3-pip
RUN apt-get update
RUN apt-get install -y cron
RUN apt-get update
COPY . /app
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
