from airflow.models import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

from datetime import datetime, timedelta
import pandas as pd
import xml.etree.ElementTree as ET
import sqlite3
import glob

log_file = "log_file.txt"
target_file = "transformed_data.csv"
db_name = "retail.db"
table_name = "sale_order"
extracted_data = None
transformed_data = None

def extract_from_csv(file_to_process):
    dataframe = pd.read_csv(file_to_process)
    return dataframe


def extract_from_json(file_to_process):
    dataframe = pd.read_json(file_to_process, lines=True)
    return dataframe


def extract_from_xml(file_to_process):
    dataframe = pd.DataFrame(columns=["store_code", "product_code", "quantity", "unit_price"])
    tree = ET.parse(file_to_process)
    root = tree.getroot()
    for sale in root:
        store_code = sale.find("store_code").text
        product_code = sale.find("product_code").text
        quantity = float(sale.find("quantity").text)
        unit_price = float(sale.find("unit_price").text)
        dataframe = pd.concat([dataframe,
                               pd.DataFrame([{
                                   "store_code": store_code,
                                   "product_code": product_code,
                                   "quantity": quantity,
                                   "unit_price": unit_price
                               }])],
                              ignore_index=True)
    return dataframe

def extract():
    extracted_data = pd.DataFrame(columns=["store_code", "product_code", "quantity", "unit_price"])

    print(1)
    for csvfile in glob.glob("*.csv"):
        print(csvfile)
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_csv(csvfile))], ignore_index=True)

    for jsonfile in glob.glob("*.json"):
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_json(jsonfile))], ignore_index=True)

    for xmlfile in glob.glob("*.xml"):
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_xml(xmlfile))], ignore_index=True)

    extracted_data.to_csv(target_file, index=False)
    print(extracted_data)

def transform():
    data = pd.read_csv(target_file)
    data['subtotal'] = data.quantity * data.unit_price
    data.to_csv(target_file, index=False)

def load_data():
    data = pd.read_csv(target_file)
    sql_connection = sqlite3.connect(db_name)
    data.to_sql(table_name, sql_connection, if_exists="replace", index=False)
    sql_connection.close()

default_args = {
    'owner': 'Your Name',
    'start_date': days_ago(0),
    'email': ['your email'],
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'etl_apache_airflow',
    default_args=default_args,
    description='ETL with Apache Airflow',
    schedule_interval=timedelta(days=1)
)

execute_extract = PythonOperator(
    task_id='extract',
    python_callable=extract,
    dag=dag,
)

execute_transform = PythonOperator(
    task_id='transform',
    python_callable=transform,
    dag=dag,
)

execute_load = PythonOperator(
    task_id='load',
    python_callable=load_data,
    dag=dag
)

execute_extract >> execute_transform >> execute_load