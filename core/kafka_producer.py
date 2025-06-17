from confluent_kafka import Producer
import os, json
producer = Producer({
    "bootstrap.servers": os.getenv("KAFKA_BOOTSTRAP_SERVERS", "kafka:9092")
})

async def send_error_to_kafka(exc, request):
    print(exc)