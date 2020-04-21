FROM ubuntu:16.04
RUN apt-get -qq update && apt-get -qq install --assume-yes "build-essential" "python3-dev" "python3-pip" 
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY ./zingmp3Crawler /app
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
ADD ./Music /app/Music
CMD ["python3", "/app/consumer.py"]