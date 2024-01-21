Real-Time Economic Indicator Dashboard
==============================

Demo: https://pintoza-real-time-indicators-home-slo8fp.streamlit.app/

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
- This project creates an analytics engineering dashboard for visualizing key economic indicators. It aims to provide up-to-date information on leading, lagging, and coincident economic indicators, reflecting the latest economic trends and data releases. 
- The initiative involves the aggregation of data from various authoritative economic sources, focusing on the real-time update and visualization of these indicators.

### Objectives
- Develop a platform that showcases updated economic indicators, making complex data accessible and interpretable.
- Empower users with the ability to analyze trends in economic data through interactive visualizations.

### Data Sources
- The data is sourced from several economic sources, (see Inidicators list above), although the data is pulled from two main sources:
  - Federal Reserve Economic Data (FRED) API via the [fredapi](https://github.com/mortada/fredapi)
  - Survey of Consumers, University of Michigan via the [Survey of Consumers](http://www.sca.isr.umich.edu/)


## Architecture and Technologies

### Overview
- This project employs a robust data pipeline that extracts, processes, and loads data into a streamlit web app and uses cron jobs to ensure updated and clean data is always available.
- The updates are set to run daily at 11 AM EST, ensuring that the data is always up-to-date.

### Technologies
- **Data Extraction and Loading**:
  - Python scripts for automated data extraction and loading.
  - Cron jobs for scheduling daily updates.
- **Data Visualization**:
  - Plotly for creating interactive data visualizations.
- **Web Application**:
  - Streamlit for building the interactive web application.

## Installation and Usage

### Prerequisites
- Python 3.x
- Streamlit
- FRED API Key
- Other Python packages (see requirements.txt)

### Setup
- Instructions on setting up the database, environment variables, and running the Python scripts.

### Running the Application
- Steps to start the Streamlit server and access the web application.

## Contributions and Acknowledgements

- Details on how others can contribute to the project.
- Acknowledgements for any third-party resources or contributors.

## License

- This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.


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

