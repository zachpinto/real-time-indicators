import streamlit as st
import pandas as pd
import plotly.express as px
import os


# Function to retrieve data for a specific indicator
def get_indicator_data(indicator_name):
    # Define the path to the processed data directory
    processed_data_dir = '/Users/pintoza/Desktop/dev/analytics-engineering/real-time-indicators/data/processed/lagging_indicators'

    # Build the file path
    file_path = os.path.join(processed_data_dir, f'{indicator_name}.csv')

    # Read data from the corresponding CSV file
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        return df
    else:
        # Return an empty DataFrame if file does not exist
        return pd.DataFrame()


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

formatting_rules = {
    "avg_weeks_unemployment": "keep_same",
    "commercial_industrial_loans": "to_trillion",
    "cpi_all": "keep_same",
    "unit_labor_costs_all": "keep_same",
    "manufacture_inventory_sales_ratio": "keep_same",
    "consumer_credit_pi": "to_percentage",
    "bank_prime_loan": "to_percentage",
}

def format_value(value, format_type):
    if format_type == 'to_million':
        return f"{value / 1000:.2f}M"
    elif format_type == 'millions_to_billion_with_dollar':
        return f"${value / 1000:.2f}B"
    elif format_type == 'thousands_to_million':
        return f"{value / 1000:.2f}M"  # Format as millions with 'M'
    elif format_type == 'to_percentage':
        return f"{value:.2f}%"
    elif format_type == 'to_thousand':
        return f"{value / 1000:.0f}K"
    elif format_type == 'keep_same':
        return value
    elif format_type == 'to_trillion':
        return f"${value / 1000:.2f}T"
    else:
        return value

def get_y_axis_label(format_type):
    if format_type == 'to_million':
        return 'Value (Millions)'
    elif format_type == 'millions_to_billion_with_dollar':
        return 'Value (Billions)'
    elif format_type == 'thousands_to_million':
        return 'Value (Millions)'
    elif format_type == 'to_percentage':
        return 'Percentage (%)'
    elif format_type == 'to_thousand':
        return 'Value (Thousands)'
    elif format_type == 'to_trillion':
        return 'Value (Trillions)'
    else:
        return 'Value'

def transform_value_for_plotting(value, format_type):
    if format_type == 'to_million':
        return value / 1000  # Convert to millions
    elif format_type == 'millions_to_billion_with_dollar':
        return value / 1000  # Convert to billions
    elif format_type == 'thousands_to_million':
        return value / 1000  # Convert to millions for plotting
    elif format_type == 'to_percentage':
        return value  # Keep as is, since it's already a percentage
    elif format_type == 'to_thousand':
        return value / 1000  # Convert to thousands for plotting
    elif format_type == 'to_trillion':
        return value / 1000  # Convert millions to trillions
    else:
        return value


for indicator in indicators:
    df = get_indicator_data(indicator)
    format_type = formatting_rules.get(indicator, "keep_same")

    df['plot_value'] = df['value'].apply(lambda x: transform_value_for_plotting(x, format_type))
    df['display_value'] = df['value'].apply(lambda x: format_value(x, format_type))

    title = indicator_titles.get(indicator, "Indicator")
    report_url = report_links.get(indicator, "#")

    if not df.empty:
        most_recent_value = df.iloc[-1]['display_value']
        most_recent_date = df.iloc[-1]['date']
        y_axis_label = get_y_axis_label(format_type)

        st.subheader(f"{title}")
        st.markdown(f"*Most recent value: {most_recent_value} on {most_recent_date}*")
        st.markdown(f"[Read the entire report here]({report_url})", unsafe_allow_html=True)

        fig = px.line(df, x='date', y='plot_value', title=title)
        fig.update_layout(xaxis_title='Date', yaxis_title=y_axis_label)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.subheader(f"{title} (No data available)")

    st.write("---")