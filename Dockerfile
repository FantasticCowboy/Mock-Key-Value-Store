FROM ubuntu:22.04
RUN apt update
RUN apt install python3 python3-pip -y

WORKDIR /home
COPY src src
COPY ./requirements.txt ./requirements.txt
COPY ./requirements-dev.txt ./requirements-dev.txt
COPY etc etc
EXPOSE 5000
RUN pip3 install -r ./requirements-dev.txt
