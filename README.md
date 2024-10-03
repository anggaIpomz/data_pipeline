# ETL CDC:

 - curl -X DELETE http://localhost:8083/connectors/postgres-connector
 - curl -X POST http://localhost:8083/connectors -H "Content-Type: application/json" -d {postgres_connector.json}
 - change the postgresql.conf, listen_addresses = '*', wal_level = logical
 - change the pg_hba.conf

   host    all             all             0.0.0.0/0            md5


##Kafka commands
- docker exec -it debezium_kafka_1 /bin/kafka-consumer-groups --bootstrap-server kafka:9092 --describe --help
- docker exec -it debezium_kafka_1 /bin/kafka-consumer-groups --bootstrap-server kafka:9092 --describe --all-groups
- docker exec -it debezium_kafka_1 /bin/kafka-consumer-groups --bootstrap-server kafka:9092 --describe --all-groups --all-topics
- docker exec -it debezium_kafka_1 /bin/kafka-consumer-groups --bootstrap-server kafka:9092 --describe --group your_group_name

- docker exec -it debezium_kafka_1 /bin/kafka-console-consumer --bootstrap-server kafka:9092 --topic dbserver1.public.customer --from-beginning
- docker exec -it debezium_kafka_1 /bin/kafka-console-consumer --bootstrap-server kafka:9092 --topic dbserver1.public.customer --group your_group_name --from-beginning


- docker exec -it debezium_kafka_1 /bin/kafka-console-producer --bootstrap-server kafka:9092 --topic dbserver1.public.customer
