from aiokafka import AIOKafkaProducer
from sqlmodel import Session
from app.db_engine import engine

# create app consumer dependencies 
# Kafka Producer as a dependency
# 80- product-service\app\main.py    
async def get_kafka_producer():
    producer = AIOKafkaProducer(bootstrap_servers='broker:19092')
    await producer.start()
    try:
        yield producer
    finally:
        await producer.stop()

def get_session():
    with Session(engine) as session:
        yield session

