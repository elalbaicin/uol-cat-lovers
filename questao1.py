# Libraries
import requests
import pandas as pd
import json

# Base URL
base_url = "https://cat-fact.herokuapp.com"

# Amount of cat facts
amount = 50

# Endpoint
endpoint = f"/facts/random?animal_type=cat&amount={amount}"

# Requested URL
url = f"{base_url}{endpoint}"

# Request
response = requests.get(url)

# Throw an exception if status response is not 200
if response.status_code != 200:
  
  error_status = response.status_code
  
  error_text = str(response.text)
  
  raise Exception(f"Error {error_status}: {error_text}")

# Raw content
raw_content = response.content

# Raw dictionary
raw_dict = json.loads(raw_content)

# Raw DataFrame
raw_df = pd.DataFrame(raw_dict)

# Write csv file; use ";" as delimiter, as status col is a json
raw_df.to_csv("local-file.csv", sep = ";", index = False)

