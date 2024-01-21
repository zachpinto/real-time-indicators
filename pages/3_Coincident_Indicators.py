import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Function to retrieve data for a specific indicator
def get_indicator_data(indicator_name):
    # Define the path to the processed data directory
    processed_data_dir = 'data/processed/coincident_indicators'

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

report_links = {
    "industrial_prod_index": "http://www.federalreserve.gov/releases/g17/",
    "manufacture_trade_sales": "https://fred.stlouisfed.org/series/CMRMTSPL",
    "pi_exclude_transfers": "https://www.bea.gov/data/income-saving/personal-income",
    "total_employees_nonfarm": "https://www.bls.gov/ces/"
}

formatting_rules = {
    "industrial_prod_index": "keep_same",
    "manufacture_trade_sales": "manufacture_trade_sales",
    "pi_exclude_transfers": "to_trillion",
    "total_employees_nonfarm": "to_million",
}

def format_value(value, format_type):
    if format_type == 'to_million':
        return f"{value / 1000:.2f}M"
    elif format_type == 'millions_to_billion_with_dollar':
        return f"${value / 1000:.2f}B"
    elif format_type == 'thousands_to_million':
        return f"{value / 1000:.2f}M"  # Format as millions with 'M'
    elif format_type == 'to_percentage':
        return f"{value}%"
    elif indicator == 'total_employees_nonfarm':
        return f"{value / 1000:.2f}M"
    elif format_type == 'keep_same':
        return f"{value :.2f}"
    if indicator == 'manufacture_trade_sales':
        return f"${value / 1000000:.2f}T"  # Assuming raw data is in billions, format as trillions
    elif formatting_rules[indicator] == 'to_trillion':
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
    elif format_type == 'to_trillion':
        return 'Value (Trillions)'
    elif indicator == 'manufacture_trade_sales':
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
    elif indicator == 'manufacture_trade_sales':
        return value / 1000000  # Assuming raw data is in billions, convert to trillions
    elif formatting_rules[indicator] == 'to_trillion':
        return value / 1000  # Convert millions to trillions
    # Convert millions to trillions
    else:
        return value


for indicator in indicators:
    df = get_indicator_data(indicator)
    format_type = formatting_rules[indicator]

    df['plot_value'] = df['value'].apply(lambda x: transform_value_for_plotting(x, format_type))
    df['display_value'] = df['value'].apply(lambda x: format_value(x, indicator))

    title = indicator_titles.get(indicator, "Indicator")
    report_url = report_links.get(indicator, "#")

    if not df.empty:
        most_recent_value = df.iloc[-1]['display_value']
        most_recent_date = df.iloc[-1]['date']
        y_axis_label = get_y_axis_label(format_type)  # Now correctly using format_type

        st.subheader(f"{title}")
        st.markdown(f"*Most recent value: {most_recent_value} on {most_recent_date}*")
        st.markdown(f"[Read the entire report here]({report_url})", unsafe_allow_html=True)

        fig = px.line(df, x='date', y='plot_value', title=title)
        fig.update_layout(xaxis_title='Date', yaxis_title=y_axis_label)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.subheader(f"{title} (No data available)")

    st.write("---")
