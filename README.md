# ETL Script Documentation
## Overview
This ETL (Extract, Transform, Load) script processes CSV, JSON, and XML files to extract data, transform it into the desired format, and load it into a CSV file. Additionally, it logs the progress of each step to a log file.


![ETL_diagram](https://github.com/user-attachments/assets/8eae55cf-763b-4a07-9207-cc85954eb1d4)

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
```bash
pip install pandas
```

## Usage
1. Place your CSV, JSON, and XML files in the same directory as the script.

2. Run the script:
```bash
python3 etl_script.py
```

3. Check the log_file.txt for the progress of each step.

4. The transformed data will be saved to transformed_data.csv.
