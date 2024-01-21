Real-Time Economic Indicator Dashboard
==============================

Demo: 

## Indicators:
### Leading Indicators
- [Average Weekly Hours of All Employees, Manufacturing](https://fred.stlouisfed.org/series/AWHAEMAN)
- [Average Weekly Initial Jobless Claims](https://fred.stlouisfed.org/series/ICSA)
- [Manufacturers' New Orders: Consumer Goods](https://fred.stlouisfed.org/series/ACOGNO)
- [Manufacturers' New Orders: Non-defense Capital Goods](https://fred.stlouisfed.org/series/ANDENO)
- [Building Permits: New Privately Owned Housing Units](https://fred.stlouisfed.org/series/PERMIT)
- [S&P 500 Stock Price Index](https://fred.stlouisfed.org/series/SP500)
- [Interest Rate Spread: 10-Year Treasury Constant Maturity vs. Federal Funds Rate](https://fred.stlouisfed.org/series/T10YFF)
- [Average Consumer Expectations for Business Conditions](https://data.sca.isr.umich.edu/data-archive/mine.php#)
### Lagging Indicators
- [Average Weeks Unemployment](https://fred.stlouisfed.org/series/UEMPMEAN)
- [Commercial and Industrial Loans, All Commercial Banks](https://fred.stlouisfed.org/series/BUSLOANS)
- [Consumer Price Index for All Urban Consumers: All Items](https://fred.stlouisfed.org/series/CPIAUCSL)
- [Unit Labor Costs for All Workers](https://fred.stlouisfed.org/series/ULCNFB)
- [Manufacturers' Inventories to Sales Ratio](https://fred.stlouisfed.org/series/MNFCTRIRSA)
- [Consumer Credit as a Percentage of Disposable Personal Income](https://fred.stlouisfed.org/series/BOGZ1FL153166006Q)
- [Bank Prime Loan Rate](https://fred.stlouisfed.org/series/DPRIME)
### Coincident Indicators
- [Total Employees on Non-farm Payrolls](https://fred.stlouisfed.org/series/PAYEMS)
- [Personal Income excluding current Transfer Receipts](https://fred.stlouisfed.org/series/W875RX1)
- [Industrial Production Index](https://fred.stlouisfed.org/series/INDPRO)
- [Manufacturing and Trade Industries Sales](https://fred.stlouisfed.org/series/CMRMTSPL)

## Introduction
### Background
- This project focuses on building an analytics engineering solution to visualize leading, lagging, and coincident economic indicators. The primary goal is to provide real-time economic data and report updates from a list of economic indicators as they are released. All indicators are updated daily, weekly, monthly or quarterly, depending on the frequency of the data source.
### Objectives
- To create a user-friendly platform that displays up-to-date economic indicators.
- To assist users in making informed decisions by providing historical and current data visualizations.
- To integrate real-time news feeds that relate to the displayed economic indicators.

### Research Questions
- How do various economic indicators evolve over time?
- What are the relationships among different economic indicators?
- How does the latest news correlate with changes in these indicators?

## Data

### Data Sources
- The data is sourced from multiple reliable financial and economic databases, including but not limited to:
  - Federal Reserve Economic Data (FRED)
  - U.S. Bureau of Labor Statistics
  - U.S. Census Bureau
- Real-time news articles are fetched using news feed APIs from established news outlets.

### Data Attributes
- Economic indicators include, but are not limited to:
  - Total nonfarm payrolls
  - Unemployment rate
  - Inflation rate
  - Consumer Price Index (CPI)
  - Gross Domestic Product (GDP)
- Each dataset includes attributes such as date, numerical values, and relevant descriptors.

## Architecture and Technologies

### Overview
- This project employs a robust data pipeline that extracts, processes, and loads data into a PostgreSQL database, ensuring updated and clean data is always available.

### Technologies
- **Data Extraction and Loading**:
  - Python scripts for automated data extraction and loading.
  - Cron jobs for scheduling daily updates.
- **Database**:
  - PostgreSQL for data storage.
- **Data Visualization**:
  - Plotly for creating interactive data visualizations.
- **Web Application**:
  - Streamlit for building the interactive web application.
- **Deployment**:
  - GitHub for version control and deployment via Streamlit.

## Installation and Usage

### Prerequisites
- Python 3.x
- PostgreSQL
- Access to economic data sources and news API.

### Setup
- Instructions on setting up the database, environment variables, and running the Python scripts.

### Running the Application
- Steps to start the Streamlit server and access the web application.

## Contributions and Acknowledgements

- Details on how others can contribute to the project.
- Acknowledgements for any third-party resources or contributors.

## License

- Information about the project's license.


Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   │
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

