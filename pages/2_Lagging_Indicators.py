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
st.set_page_config(page_title="Lagging Economic Indicators", layout="wide")

# Page Title
st.title("Lagging Economic Indicators")

# Line separator
st.markdown("---")

# For each leading indicator
indicators = ["avg_weeks_unemployment", "commercial_industrial_loans", "cpi_all", "unit_labor_costs_all",
              "manufacture_inventory_sales_ratio", "consumer_credit_pi", "bank_prime_loan"]

indicator_titles = {
    "avg_weeks_unemployment": "Average Weeks on Unemployment Insurance (Updated Monthly)",
    "commercial_industrial_loans": "Commercial and Industrial Loans, All Commercial Banks (Updated Monthly)",
    "cpi_all": "Consumer Price Index for All Urban Consumers: All Items (Updated Monthly)",
    "unit_labor_costs_all": "Unit Labor Costs for All Workers (Updated Quarterly)",
    "manufacture_inventory_sales_ratio": "Manufacturers' Inventories to Sales Ratio (Updated Monthly)",
    "consumer_credit_pi": "Consumer Credit as a Percentage of Disposable Personal Income (Updated Quarterly)",
    "bank_prime_loan": "Bank Prime Loan Rate (Updated Daily)",
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

