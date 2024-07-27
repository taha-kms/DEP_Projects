from extract import Extract
from transform import Transform
from load import Load

# URL of the page to scrape
url = 'https://en.wikipedia.org/wiki/List_of_largest_banks'

# Create an Extract object and extract information
extractor = Extract(url)
extractor.extract_information()
data = extractor.to_data()

transformer = Transform(data)
dataframe = transformer.to_dataFrame()

print(dataframe)

load = Load(dataframe)
load.to_sql()
load.to_json()
load.to_csv()
