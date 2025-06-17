from confluent_kafka import Consumer
import os
consumer = Consumer({
    "bootstrap.servers": os.getenv("KAFKA_BOOTSTRAP_SERVERS", "kafka:9092"),
    "group.id": "logging",
    "auto.offset.reset": "latest"
})

consumer.subscribe(["errors"])

def consume_forever():
    while True:
        msg = consumer.poll(1.0)  # wait up to 1 sec
        if msg is None:
            continue
        if msg.error():
            print("⚠️ Consumer error:", msg.error())
            continue

        print(f"Message Received")

