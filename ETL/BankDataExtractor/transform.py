import json
import requests
import pandas as pd
from log import Log

class Transform:
    
    def __init__(self, data: dict) -> None:
        # Initialize the class with raw data
        self.logger = Log()     
        self.rawData = pd.DataFrame(data)
        self.conversion_rates = self.get_conversion_rates()
        self.df = self.feedNewData()
    def feedNewData(self):


        data = {
            'Name': [],
            'Country': [],
            'MarketCap_USD': [],
            'MarketCap_GBP': [],
            'MarketCap_EUR': [],
            'MarketCap_INR': [],
        }

        # Extract raw data lists
        names = self.rawData['Name']
        market_caps = self.rawData['MarketCap']
        countries = self.rawData['Country']

        # Populate the new data dictionary
        for name, market_cap, country in zip(names, market_caps, countries):

            try:
                market_cap = float(market_cap)
            except ValueError:
                self.logger.error(f"Invalid market_cap value: {market_cap}")
                continue


            data['Name'].append(name)
            data['Country'].append(country)
            data['MarketCap_USD'].append(float(market_cap))
            data['MarketCap_GBP'].append(round(float(market_cap) * self.conversion_rates.get('GBP', 0), 2))
            data['MarketCap_EUR'].append(round(float(market_cap) * self.conversion_rates.get('EUR', 0), 2))
            data['MarketCap_INR'].append(round(float(market_cap) * self.conversion_rates.get('INR', 0), 2))
            self.logger.info(f"Transformed: {data['Name'][-1]}, USD {data['MarketCap_USD'][-1]}")

        return pd.DataFrame(data)

    def getNewPrices(self):
        url = "https://api.currencyapi.com/v3/latest"
        headers = {'apikey': 'API_KEY'}
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raises HTTPError for bad responses
            return response.json()
        except requests.RequestException as e:
            self.logger.error(f"Error fetching new prices: {e}")
            return None

    def get_conversion_rates(self):
        data = self.getNewPrices()
        if data:
            try:
                return {
                    "USD": 1,
                    "GBP": data['data']['GBP']['value'],
                    "EUR": data['data']['EUR']['value'],
                    "INR": data['data']['INR']['value']
                }
            except KeyError as e:
                self.logger.error(f"Error parsing conversion rates: {e}")
                return {
                    "USD": 1,
                    "GBP": 0,
                    "EUR": 0,
                    "INR": 0
                }
        else:
            return {
                "USD": 1,
                "GBP": 0,
                "EUR": 0,
                "INR": 0
            }

    def to_dataFrame(self):
        return self.df
