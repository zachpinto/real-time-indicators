import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Function to retrieve data for a specific indicator
def get_indicator_data(indicator_name):
    processed_data_dir = '/Users/pintoza/Desktop/dev/analytics-engineering/real-time-indicators/data/processed/leading_indicators'
    file_path = os.path.join(processed_data_dir, f'{indicator_name}.csv')
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    else:
        return pd.DataFrame()

st.set_page_config(page_title="Leading Economic Indicators", layout="wide")
st.title("Leading Economic Indicators")
st.markdown("---")

# For each leading indicator
indicators = ["avg_weekly_hours_manufacture", "avg_weekly_initial_jobless_claims", "manufacturer_new_orders_consumer",
              "manufacture_new_order_capital", "building_permits", "sp_500_index", "interest_rate_spread",
              "avg_consumer_expectations"]

indicator_titles = {
    "avg_weekly_hours_manufacture": "Average Weekly Hours in Manufacturing (Updated Monthly)",
    "avg_weekly_initial_jobless_claims": "Average Weekly Initial Jobless Claims (Updated Weekly)",
    "manufacturer_new_orders_consumer": "New Orders for Consumer Goods Manufacturing (Updated Monthly)",
    "manufacture_new_order_capital": "New Orders for Capital Goods Manufacturing (Updated Monthly)",
    "building_permits": "Building Permits Issued (Updated Monthly)",
    "sp_500_index": "S&P 500 Index (Updated Daily)",
    "interest_rate_spread": "Interest Rate Spread (Updated Daily)",
    "avg_consumer_expectations": "Average Consumer Expectations (Updated Monthly)"
}

report_links = {
    "avg_weekly_hours_manufacture": "https://www.bls.gov/ces/",
    "avg_weekly_initial_jobless_claims": "https://www.dol.gov/ui/data.pdf",
    "manufacturer_new_orders_consumer": "https://www.census.gov/manufacturing/m3/index.html",
    "manufacture_new_order_capital": "http://www.census.gov/indicator/www/m3/",
    "building_permits": "https://www.census.gov/construction/nrc/index.html",
    "sp_500_index": "https://www.spglobal.com/spdji/en/indices/equity/sp-500/#overview",
    "interest_rate_spread": "https://fred.stlouisfed.org/series/T10YFF",
    "avg_consumer_expectations": "https://data.sca.isr.umich.edu/reports.php"
}

formatting_rules = {
    "avg_weekly_hours_manufacture": "keep_same",
    "avg_weekly_initial_jobless_claims": "to_thousand",
    "manufacturer_new_orders_consumer": "millions_to_billion_with_dollar",
    "manufacture_new_order_capital": "millions_to_billion_with_dollar",
    "building_permits": "thousands_to_million",
    "sp_500_index": "keep_same",
    "interest_rate_spread": "to_percentage",
    "avg_consumer_expectations": "to_percentage"
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
    elif format_type == 'to_thousand':
        return f"{value / 1000:.0f}K"
    elif format_type == 'keep_same':
        return value
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
    else:
        return value  # Default, no transformation


for indicator in indicators:
    df = get_indicator_data(indicator)
    format_type = formatting_rules.get(indicator, "keep_same")

    title = indicator_titles[indicator]  # Moved outside of the if statement
    report_url = report_links[indicator]  # Moved outside of the if statement

    if not df.empty:
        df['plot_value'] = df['value'].apply(lambda x: transform_value_for_plotting(x, format_type))
        df['display_value'] = df['value'].apply(lambda x: format_value(x, format_type))

        most_recent_value = df.iloc[-1]['display_value']
        most_recent_date = df.iloc[-1]['date']
        y_axis_label = get_y_axis_label(format_type)

        st.subheader(title)
        st.markdown(f"*Most recent value: {most_recent_value} on {most_recent_date}*")
        st.markdown(f"[Read the entire report here]({report_url})", unsafe_allow_html=True)

        fig = px.line(df, x='date', y='plot_value', title=title)
        fig.update_layout(xaxis_title='Date', yaxis_title=y_axis_label)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.subheader(f"{title} (No data available)")

st.write("---")
