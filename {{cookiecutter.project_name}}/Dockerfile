FROM ubuntu

RUN apt update && apt upgrade -y

{% if cookiecutter.db_backend == "mysql" %}

RUN apt install -y python3-pip default-libmysqlclient-dev
RUN pip3 install django django-probes mysqlclient

{% elif cookiecutter.db_backend == "postgresql" %}

RUN apt install -y python3-pip libpq-dev
RUN pip3 install django django-probes psycopg2

{% endif %}