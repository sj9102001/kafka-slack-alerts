from confluent_kafka import Producer
import os, json
producer = Producer({
    "bootstrap.servers": os.getenv("KAFKA_BOOTSTRAP_SERVERS", "kafka:9092")
})

async def send_error_to_kafka(exc, request):
    payload = {
        "path": request.url.path,
        "method": request.method,
        "error": str(exc)
    }
    producer.produce("errors", json.dumps(payload).encode())
    producer.flush()