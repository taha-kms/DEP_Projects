import pandas as pd
import sqlite3
from log import Log

class Load:

    def __init__(self, df: pd.DataFrame) -> None:
        self.df = df
        self.db_name = 'files/bankdb.db'
        self.tb_name = 'marketCap_tb'
        self.json_name = 'files/marketcap.json'
        self.csv_name = 'files/marketcap.csv'
        self.logger = Log()

    def to_sql(self):
        try:
            with sqlite3.connect(self.db_name) as conn:
                create_table_query = f"""
                CREATE TABLE IF NOT EXISTS {self.tb_name} (
                    Name TEXT,
                    Country TEXT,
                    MarketCap_USD REAL,
                    MarketCap_GBP REAL,
                    MarketCap_EUR REAL,
                    MarketCap_INR REAL
                )
                """
                conn.execute(create_table_query)
                self.df.to_sql(self.tb_name, conn, if_exists='replace', index=False)
                conn.commit()
            self.logger.info(f"Data saved to {self.db_name} in table {self.tb_name}.")
        except sqlite3.Error as e:
            self.logger.error(f"An error occurred while saving to SQLite: {e}")

    def to_json(self):
        try:
            self.df.to_json(self.json_name, orient='records', lines=True)
            self.logger.info(f"Data saved to {self.json_name}.")
        except Exception as e:
            self.logger.error(f"An error occurred while saving to JSON: {e}")

    def to_csv(self):
        try:
            self.df.to_csv(self.csv_name, index=False)
            self.logger.info(f"Data saved to {self.csv_name}.")
        except Exception as e:
            self.logger.error(f"An error occurred while saving to CSV: {e}")
