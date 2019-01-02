FROM python:2.7
LABEL maintainer "Andrea Cesarini <andrea.cesarini85@gmail.com>"
RUN apt-get update
RUN mkdir /elezioni
WORKDIR /elezioni
COPY . /elezioni
RUN pip install --no-cache-dir -r requirements.txt
ENV FLASK_ENV="docker"
ENV SETTINGS="/elezioni/config/config.py"
EXPOSE 5000
