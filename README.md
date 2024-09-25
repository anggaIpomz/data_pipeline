# ETL CDC:

 curl -X DELETE http://localhost:8083/connectors/postgres-connector
 curl -X POST http://localhost:8083/connectors -H "Content-Type: application/json" -d {postgres_connector.json}
