# ETL Script Documentation
## Overview
This ETL (Extract, Transform, Load) script extracts information about the largest banks from a Wikipedia page, transforms the market capitalization data into different currencies, and loads the transformed data into both a CSV file and an SQLite database. It also logs the progress of each step to a log file.

## Prerequisites
- Python 3.x
- Pandas library
- BeautifulSoup library
- Requests library
- SQLite3 library
- NumPy library
```bash
pip install pandas bs4
```

## Usage
1. Run the script:
```bash
python3 etl_script.py
```

3. Check the log_file.txt for the progress of each step.

4. The transformed data will be saved to Largest_banks_data.csv and Banks.db.
