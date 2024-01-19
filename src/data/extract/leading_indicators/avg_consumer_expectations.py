import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime


# Get current month and year
current_month = datetime.now().month
current_year = datetime.now().year

# URL for the data
url = "https://data.sca.isr.umich.edu/data-archive/mine.php#"

# Send HTTP request to the URL
response = requests.get(url)

# Parsing webpage content
soup = BeautifulSoup(response.content, "html.parser")

# Find table containing the data
div = soup.find("div", class_="grid_12 output")

# Initialize list to store data
data = []

# Loop through table rows
if div:
    table = div.find("table")
    if table:
        for row in table.find_all('tr')[1:]:
            cols = row.find_all('td')
            if len(cols) == 3:
                try:
                    month = int(cols[0].text.strip())
                    year = int(cols[1].text.strip())
                    index = float(cols[2].text.strip())

                    # Check if the date is within the last 10 years
                    if (year > current_year - 10) or (year == current_year - 10 and month >= current_month):
                        data.append({'Month': month, 'Year': year, 'Index': index})
                except ValueError:
                    continue
    else:
        print("Error: Table not found in the div")
else:
    print("Error: Div with class 'grid_12 output' not found")


# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("/Users/pintoza/Desktop/dev/analytics-engineering/real-time-indicators/data/raw/"
          "leading_indicators/avg_consumer_expectations.csv", index=False)
