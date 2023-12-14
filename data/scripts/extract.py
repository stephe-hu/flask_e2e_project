import requests
import pandas as pd

# extract data from NYC Open Data API
url = "https://data.cityofnewyork.us/resource/jb7j-dtam.json?$query=SELECT%0A%20%20%60year%60%2C%0A%20%20%60leading_cause%60%2C%0A%20%20%60sex%60%2C%0A%20%20%60race_ethnicity%60%2C%0A%20%20%60deaths%60%2C%0A%20%20%60death_rate%60%2C%0A%20%20%60age_adjusted_death_rate%60%0AORDER%20BY%20%60year%60%20DESC%20NULL%20FIRST"
response = requests.get(url)
data = response.json()

# preview data
df = pd.DataFrame(data)
df.columns

# save data as csv in data/raw
df.to_csv('data/raw/NYC_Leading_Causes_of_Death.csv', index=False)
