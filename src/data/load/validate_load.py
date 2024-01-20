import os
import pandas as pd
import psycopg2
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Database connection parameters from environment variables
db_username = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')

# Establish a connection to the database
connection_string = f"postgresql+psycopg2://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"
engine = create_engine(connection_string)

# Function to get all table names from the database
def get_all_tables(engine):
    query = "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';"
    tables = pd.read_sql_query(query, engine)
    return tables['table_name'].tolist()

# Function to query the database and return a DataFrame
def query_db(sql_query, engine):
    return pd.read_sql_query(sql_query, engine)

# Fetch all table names
tables = get_all_tables(engine)

# Iterate over each table and check the first few rows
for table in tables:
    query = f"SELECT * FROM {table} LIMIT 5;"
    df = query_db(query, engine)
    print(f"First 5 rows from {table}:\n{df}\n")

# Check the row counts for each table
for table in tables:
    query = f"SELECT COUNT(*) FROM {table};"
    count_df = query_db(query, engine)
    print(f"Total rows in {table}: {count_df.iloc[0][0]}")
