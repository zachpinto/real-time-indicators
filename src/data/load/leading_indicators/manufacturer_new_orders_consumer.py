import pandas as pd
import psycopg2
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')

# Establish a connection to the database
engine = create_engine(f'postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

# Path to your CSV file
csv_file_path = '/Users/pintoza/Desktop/dev/analytics-engineering/real-time-indicators/data/processed/leading_indicators/manufacturer_new_orders_consumer.csv'

# Load data from CSV file into DataFrame
data_df = pd.read_csv(csv_file_path)

# Table name in the database
table_name = 'manufacture_new_orders_consumer'

# Load data from DataFrame to PostgreSQL table
data_df.to_sql(table_name, engine, if_exists='replace', index=False)

print("Data loaded successfully")
