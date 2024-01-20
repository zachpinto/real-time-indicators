import streamlit as st
import pandas as pd
import plotly.express as px
import psycopg2
from dotenv import load_dotenv
import os
import requests


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

report_links = {
    "avg_weeks_unemployment": "https://www.bls.gov/ces/",
    "commercial_industrial_loans": "https://www.federalreserve.gov/releases/h8/",
    "cpi_all": "https://www.bls.gov/cpi/",
    "unit_labor_costs_all": "https://www.bls.gov/productivity/home.htm",
    "manufacture_inventory_sales_ratio": "https://www.census.gov/mtis/index.html",
    "consumer_credit_pi": "https://www.federalreserve.gov/releases/z1/i",
    "bank_prime_loan": "https://www.federalreserve.gov/releases/h15/",
}

for indicator in indicators:
    df = get_indicator_data(indicator)
    title = indicator_titles.get(indicator, "Indicator")
    report_url = report_links.get(indicator, "#")  # Fallback URL if none is provided

    if not df.empty:
        # Assuming the DataFrame is sorted by date, get the most recent value
        most_recent_value = df.iloc[-1]['value']  # Get the last row's value
        most_recent_date = df.iloc[-1]['date']  # Get the last row's date
        st.subheader(f"{title}")
        st.markdown(f"*Most recent value: {most_recent_value} on {most_recent_date}*")
        # Display hyperlink above the chart
        st.markdown(f"[Read the entire report here]({report_url})", unsafe_allow_html=True)
    else:
        st.subheader(f"{title} (No data available)")

    # Create the line chart
    fig = px.line(df, x='date', y='value', title=title)

    # Update the labels
    fig.update_layout(
        xaxis_title='Date',
        yaxis_title='Value'
    )

    # Display the chart in full width
    st.plotly_chart(fig, use_container_width=True)

    # Add a separator
    st.write("---")
