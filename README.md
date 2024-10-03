# ETL CDC:

 - curl -X DELETE http://localhost:8083/connectors/postgres-connector
 - curl -X POST http://localhost:8083/connectors -H "Content-Type: application/json" -d {postgres_connector.json}
 - change the postgresql.conf, listen_addresses = '*', wal_level = logical
 - change the pg_hba.conf

   host    all             all             0.0.0.0/0            md5
