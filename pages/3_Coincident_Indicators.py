import streamlit as st
import pandas as pd
import plotly.express as px
import psycopg2
from dotenv import load_dotenv
import os


# Load environment variables
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

# Function to connect to the database
def connect_to_db():
    conn = psycopg2.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        dbname=DB_NAME
    )
    return conn

# Function to retrieve data for a specific indicator
def get_indicator_data(indicator_name):
    conn = connect_to_db()
    query = f"SELECT * FROM {indicator_name};"  # Modify query as needed
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

# Page configuration
st.set_page_config(page_title="Coincident Economic Indicators", layout="wide")

# Page Title
st.title("Coincident Economic Indicators")

# Line separator
st.markdown("---")

# For each leading indicator
indicators = ["industrial_prod_index", "manufacture_trade_sales", "pi_exclude_transfers", "total_employees_nonfarm"]

indicator_titles = {
    "industrial_prod_index": "Industrial Production Index (Updated Monthly)",
    "manufacture_trade_sales": "Manufacturing and Trade Industries Sales (Updated Monthly)",
    "pi_exclude_transfers": "Personal Income excluding current Transfer Receipts (Updated Monthly)",
    "total_employees_nonfarm": "Total Employees on Non-farm Payrolls (Updated Monthly)",
}

for indicator in indicators:
    df = get_indicator_data(indicator)
    title = indicator_titles.get(indicator, "Indicator")  # Default title if not found

    if not df.empty:
        # Assuming the DataFrame is sorted by date, get the most recent value
        most_recent_value = df.iloc[-1]['value']  # Get the last row's value
        most_recent_date = df.iloc[-1]['date']  # Get the last row's date
        st.subheader(f"{title}")
        st.markdown(f"*Most recent value: {most_recent_value} on {most_recent_date}*")
    else:
        st.subheader(f"{title} (No data available)")

    # Create the line chart
    fig = px.line(df, x='date', y='value', title=title)

    # Update the labels
    fig.update_layout(
        xaxis_title='Date',
        yaxis_title='Value'
    )

    # Create two columns for the chart and additional content
    col1, col2 = st.columns([1, 1])  # Adjust the ratio as needed

    with col1:
        # Display the chart in the first column
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        # Additional content (like article titles) can go here
        st.write("Articles or additional information here")

    # Add a separator
    st.write("---")

