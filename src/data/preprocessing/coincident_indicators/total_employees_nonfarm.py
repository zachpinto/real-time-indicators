import pandas as pd

# Path to the raw data file
raw_data_file = '/Users/pintoza/Desktop/dev/analytics-engineering/real-time-indicators/data/raw/coincident_indicators/total_employees_nonfarm.csv'

# Load the file without headers
df = pd.read_csv(raw_data_file)

# Rename the columns
df.columns = ['date', 'value']

# Convert the date column to datetime
df['date'] = pd.to_datetime(df['date'])

# Save the file
df.to_csv('/Users/pintoza/Desktop/dev/analytics-engineering/real-time-indicators/data/processed/coincident_indicators/total_employees_nonfarm.csv', index=False)
