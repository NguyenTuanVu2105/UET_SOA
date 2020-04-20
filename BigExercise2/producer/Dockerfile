FROM python:3.7-alpine
RUN pip install pika
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY . /app
CMD ["python", "/app/producer.py"]