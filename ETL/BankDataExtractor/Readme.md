Here's a brief and comprehensive `README.md` file for your project:

---

# Bank Data Scraper

## Overview

The Bank Data Scraper is a Python-based ETL (Extract, Transform, Load) pipeline designed to scrape data about the largest banks from a Wikipedia page. The pipeline extracts information on bank names, market capitalizations, and their respective countries, transforms the data into a structured format, and finally loads it into various formats (SQLite, JSON, CSV).

## Project Structure

- `main.py`: The main script that orchestrates the ETL process.
- `extract.py`: Contains the `Extract` class responsible for scraping data from the source URL.
- `transform.py`: Contains the `Transform` class responsible for converting raw data into a pandas DataFrame.
- `load.py`: Contains the `Load` class responsible for saving the data into SQLite, JSON, and CSV formats.
- `log.py`: Contains the `Log` class for logging information and errors.

## Installation

To run this project, ensure you have Python installed along with the required packages. You can install the necessary dependencies using:

```bash
pip install pandas requests beautifulsoup4
```

## Usage

1. **Run the ETL Pipeline**: Execute the `main.py` script to start the extraction, transformation, and loading process.

```bash
python main.py
```

2. **Output Files**: After running the script, you will find the following files in the `files` directory:
    - `bankdb.db`: SQLite database containing the bank data.
    - `marketcap.json`: JSON file with the bank data in JSON format.
    - `marketcap.csv`: CSV file with the bank data in CSV format.
    - `log.txt`: Log file recording the operation and any errors encountered.

## Code Explanation

- **`extract.py`**: The `Extract` class fetches the webpage and extracts the necessary bank information using BeautifulSoup. It parses the HTML to get the bank names, market capitalization, and countries.
  
- **`transform.py`**: The `Transform` class takes the raw data and converts it into a pandas DataFrame for easy manipulation and saving.
  
- **`load.py`**: The `Load` class handles saving the DataFrame into multiple formats: SQLite database, JSON, and CSV. It also includes logging to track the process and handle any errors.
  
- **`log.py`**: The `Log` class provides a simple logging mechanism to record the information and errors encountered during the ETL process.

## Logging

Logs are saved in `files/log.txt`, and they contain information about the ETL process and any errors that occur.


Feel free to modify any details as needed to better fit your project or personal preferences!
