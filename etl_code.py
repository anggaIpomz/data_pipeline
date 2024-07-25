import glob
import pandas as pd
import xml.etree.ElementTree as ET
from datetime import datetime

log_file = "log_file.txt"
target_file = "transformed_data.csv"


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

    for csvfile in glob.glob("*.csv"):
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_csv(csvfile))], ignore_index=True)

    for jsonfile in glob.glob("*.json"):
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_json(jsonfile))], ignore_index=True)

    for xmlfile in glob.glob("*.xml"):
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_xml(xmlfile))], ignore_index=True)

    return extracted_data


def transform(data):
    data['subtotal'] = data.quantity * data.unit_price

    return data


def load_data(target_file, transformed_data):
    transformed_data.to_csv(target_file)


def log_progress(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open(log_file, "a") as f:
        f.write(timestamp + ',' + message + '\n')


log_progress("ETL Job Started")

log_progress("Extract phase Started")
extracted_data = extract()
log_progress("Extract phase Ended")

log_progress("Transform phase Started")
transformed_data = transform(extracted_data)
print("Transformed Data")
print(transformed_data)
log_progress("Transform phase Ended")

log_progress("Load phase Started")
load_data(target_file, transformed_data)
log_progress("Load phase Ended")

log_progress("ETL Job Ended")
