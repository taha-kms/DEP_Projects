import requests
import pandas as pd
from bs4 import BeautifulSoup
from log import Log

class Extract:

    def __init__(self, url) -> None:
        self.url = url
        self.content = requests.get(url).text
        self.table = BeautifulSoup(self.content, 'html.parser').find('tbody')
        self.data = {
            'Name': [],
            'MarketCap': [],
            'Country': [],
        }
        self.logger = Log()

    def extract_information(self):
        if not self.table:
            self.logger.error("No table found.")
            return

        rows = self.table.find_all('tr')

        for row in rows:
            try:
                # Extract country name
                flagicon = row.find('span', class_='flagicon')
                if flagicon:
                    country_tag = flagicon.find('span', class_='mw-image-border').a
                    country_href = country_tag['href']
                    country_name = country_href.split('/')[-1].replace('_', '')
                else:
                    continue
                # Extract bank name
                a_tags = row.find_all('a')
                if len(a_tags) > 1:
                    bank_name = a_tags[1].text
                else:
                    bank_name = "Unknown"

                # Extract market cap
                td_tags = row.find_all('td')
                if len(td_tags) > 2:
                    market_cap = td_tags[2].text.strip().replace(',', '')
                else:
                    market_cap = "Unknown"

                # Append to data dictionary
                self.data['Name'].append(bank_name)
                self.data['MarketCap'].append(market_cap)
                self.data['Country'].append(country_name)
                
                self.logger.info(f"Extracted: {bank_name}, {market_cap}, {country_name}")

            except Exception as e:
                self.logger.error(f"Error processing row: {e}")

    def to_data(self):
        return self.data
