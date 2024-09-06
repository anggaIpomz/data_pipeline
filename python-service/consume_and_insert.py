from kafka import KafkaConsumer
import clickhouse_connect
import json
from uuid_extensions import uuid7, uuid7str
from datetime import datetime


# Kafka Consumer setup
consumer = KafkaConsumer(
    'dbserver1.public.uk_price_paid',  # Ganti dengan nama topik Kafka yang sesuai
    bootstrap_servers='kafka:9092',
    #bootstrap_servers='localhost:29092',
    auto_offset_reset='earliest',
    group_id='your_group_name'
)

# ClickHouse setup
client = clickhouse_connect.get_client(host='clickhouse', port=8123)

# Consume messages from Kafka and insert into ClickHouse
for message in consumer:
    record = json.loads(message.value.decode('utf-8'))
    #record = message.value.decode('utf-8')

    operation = record['op']
    table_name = record['source']['table']
    rec_id = record['before']['id'] if record['before'] is not None else record['after']['id']

    print(operation, table_name, rec_id)

    #print(record['after'])
    #for k,v in record['after'].items():
        #print(k,v)
    #values = (record['id'], record['rec_id'], record['tableName'], record['operation'], record['ts_stamp'])
    #clickhouse_client.query(query, values)
    
    generated_id = uuid7str()
    query = """
        INSERT INTO audit_log (id, rec_id, tableName, operation, ts_stamp)
        VALUES
    """
    values = (generated_id, rec_id, table_name, operation, datetime.now())
    client.insert('audit_log', [values])
