from fredapi import Fred
import pandas as pd
import os
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

# Get API key from environment variable
api_key = os.getenv("FRED_API_KEY")

# Initialize Fred with your API key
fred = Fred(api_key=api_key)

# Fetch data series
data = fred.get_series("PAYEMS")

# Convert to DataFrame
df = pd.DataFrame(data, columns=['Value'])

# Filter data to only include the last 10 years
ten_years_ago = datetime.now() - pd.DateOffset(years=10)
df = df[df.index >= ten_years_ago]

# Save to CSV
df.to_csv("/Users/pintoza/Desktop/dev/analytics-engineering/real-time-indicators/"
          "data/raw/coincident_indicators/total_employees_nonfarm.csv")
