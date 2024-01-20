import pandas as pd

# Load the CSV file
df = pd.read_csv('/Users/pintoza/Desktop/dev/analytics-engineering/real-time-indicators/data/raw/leading_indicators/avg_consumer_expectations.csv')

# Combine 'Year' and 'Month' into a 'Date' column
df['date'] = pd.to_datetime(df[['Year', 'Month']].assign(DAY=1))

# Rename 'Index' column to 'Value'
df.rename(columns={'Index': 'value'}, inplace=True)

# Keep only 'Date' and 'Value' columns
df = df[['date', 'value']]

# Save the processed DataFrame to a new CSV file
processed_file_path = '/Users/pintoza/Desktop/dev/analytics-engineering/real-time-indicators/data/processed/leading_indicators/avg_consumer_expectations.csv'
df.to_csv(processed_file_path, index=False)
