# ETL with Apache Airflow
## Overview
This ETL (Extract, Transform, Load) script processes CSV, JSON, and XML files to extract data, transform it into the desired format, and load it into SQLite database. The process is orchestrated using Apache Airflow.


![ETL_diagram](https://github.com/user-attachments/assets/8eae55cf-763b-4a07-9207-cc85954eb1d4)

## Prerequisites
- Python 3.x
- Apache Airflow
- Pandas library
- SQLite3 library

You can install the necessary Python libraries using:
```bash
pip install pandas
```
## Airflow Setup
Ensure you have Apache Airflow installed and set up correctly. Follow the [Apache Airflow Installation Guide](https://airflow.apache.org/docs/apache-airflow/stable/installation/index.html) for detailed instructions.

### Extract
In the extraction process, this script will gather data from different sources and formats:
- POS Store data from JSON files
- Web Ecommerce data from XML files
- ERP Sales data from CSV files
  
Each file includes columns for Store Code, Product Code, Quantity, and Unit Price.

### Transform
During the transformation process, the quantity column will be multiplied by the unit price column to calculate the subtotal column.

### Load
Finally, the newly formatted data will be loaded into sqlite database.

## Prerequisites
- Python 3.x
- Pandas library

## Usage
1. Ensure you have the required files in the same directory as the script.
2. Start your Airflow web server and scheduler:
```bash
airflow webserver
airflow scheduler
```
3. Place the script (etl_apache_airflow.py) in your Airflow DAGs folder.
4. Check the Airflow web interface to monitor the DAG execution.
