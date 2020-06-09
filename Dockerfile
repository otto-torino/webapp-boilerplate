FROM debian

WORKDIR /usr/src/app

RUN apt update && apt upgrade -y
RUN apt install -y python3 python3-pip git
RUN pip3 install cookiecutter ansible
RUN echo "alias activate='source .virtualenv/bin/activate'" >> ~/.bashrc

COPY ./cookiecutter-django .