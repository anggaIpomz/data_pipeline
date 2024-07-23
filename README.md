# ETL Script Documentation
## Overview
This ETL (Extract, Transform, Load) script processes CSV, JSON, and XML files to extract data, transform it into the desired format, and load it into a CSV file. Additionally, it logs the progress of each step to a log file.

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
