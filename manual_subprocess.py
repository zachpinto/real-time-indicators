import subprocess
import time
import os

python_interpreter = "/opt/homebrew/Caskroom/miniconda/base/envs/indicators/bin/python"

# List of scripts to be executed in the specified order
extract_scripts = [
    "/Users/pintoza/Desktop/dev/analytics-engineering/real-time-indicators/src/data/extract/coincident_indicators/industrial_prod_index.py",
    "/Users/pintoza/Desktop/dev/analytics-engineering/real-time-indicators/src/data/extract/coincident_indicators/manufacture_trade_sales.py",
    "/Users/pintoza/Desktop/dev/analytics-engineering/real-time-indicators/src/data/extract/coincident_indicators/pi_exclude_transfers.py",
    "/Users/pintoza/Desktop/dev/analytics-engineering/real-time-indicators/src/data/extract/coincident_indicators/total_employees_nonfarm.py",
    "/Users/pintoza/Desktop/dev/analytics-engineering/real-time-indicators/src/data/extract/lagging_indicators/avg_weeks_unemployment.py",
    "/Users/pintoza/Desktop/dev/analytics-engineering/real-time-indicators/src/data/extract/lagging_indicators/bank_prime_loan.py",
    "/Users/pintoza/Desktop/dev/analytics-engineering/real-time-indicators/src/data/extract/lagging_indicators/consumer_credit_pi.py",
    "/Users/pintoza/Desktop/dev/analytics-engineering/real-time-indicators/src/data/extract/lagging_indicators/commercial_industrial_loans.py",
    "/Users/pintoza/Desktop/dev/analytics-engineering/real-time-indicators/src/data/extract/lagging_indicators/cpi_all.py",
    "/Users/pintoza/Desktop/dev/analytics-engineering/real-time-indicators/src/data/extract/lagging_indicators/manufacture_inventory_sales_ratio.py",
    "/Users/pintoza/Desktop/dev/analytics-engineering/real-time-indicators/src/data/extract/lagging_indicators/unit_labor_costs_all.py",
    "/Users/pintoza/Desktop/dev/analytics-engineering/real-time-indicators/src/data/extract/leading_indicators/avg_consumer_expectations.py",
    "/Users/pintoza/Desktop/dev/analytics-engineering/real-time-indicators/src/data/extract/leading_indicators/avg_weekly_hours_manufacture.py",
    "/Users/pintoza/Desktop/dev/analytics-engineering/real-time-indicators/src/data/extract/leading_indicators/avg_weekly_initial_jobless_claims.py",
    "/Users/pintoza/Desktop/dev/analytics-engineering/real-time-indicators/src/data/extract/leading_indicators/building_permits.py",
    "/Users/pintoza/Desktop/dev/analytics-engineering/real-time-indicators/src/data/extract/leading_indicators/interest_rate_spread.py",
    "/Users/pintoza/Desktop/dev/analytics-engineering/real-time-indicators/src/data/extract/leading_indicators/manufacture_new_order_capital.py",
    "/Users/pintoza/Desktop/dev/analytics-engineering/real-time-indicators/src/data/extract/leading_indicators/manufacturer_new_orders_consumer.py",
    "/Users/pintoza/Desktop/dev/analytics-engineering/real-time-indicators/src/data/extract/leading_indicators/sp_500_index.py",
]

# Execute extract scripts
for script in extract_scripts:
    subprocess.run([python_interpreter, script], env=os.environ.copy())
    time.sleep(10)  # Adjust the sleep time as needed

# Delay between extract and preprocess scripts
time.sleep(300)  # 5 minutes delay; adjust as needed

# List of preprocess scripts
preprocess_scripts = [
    "/Users/pintoza/Desktop/dev/analytics-engineering/real-time-indicators/src/data/preprocessing/coincident_indicators/industrial_prod_index.py",
    "/Users/pintoza/Desktop/dev/analytics-engineering/real-time-indicators/src/data/preprocessing/coincident_indicators/manufacture_trade_sales.py",
    "/Users/pintoza/Desktop/dev/analytics-engineering/real-time-indicators/src/data/preprocessing/coincident_indicators/pi_exclude_transfers.py",
    "/Users/pintoza/Desktop/dev/analytics-engineering/real-time-indicators/src/data/preprocessing/coincident_indicators/total_employees_nonfarm.py",
    "/Users/pintoza/Desktop/dev/analytics-engineering/real-time-indicators/src/data/preprocessing/lagging_indicators/avg_weeks_unemployment.py",
    "/Users/pintoza/Desktop/dev/analytics-engineering/real-time-indicators/src/data/preprocessing/lagging_indicators/bank_prime_loan.py",
    "/Users/pintoza/Desktop/dev/analytics-engineering/real-time-indicators/src/data/preprocessing/lagging_indicators/consumer_credit_pi.py",
    "/Users/pintoza/Desktop/dev/analytics-engineering/real-time-indicators/src/data/preprocessing/lagging_indicators/commercial_industrial_loans.py",
    "/Users/pintoza/Desktop/dev/analytics-engineering/real-time-indicators/src/data/preprocessing/lagging_indicators/cpi_all.py",
    "/Users/pintoza/Desktop/dev/analytics-engineering/real-time-indicators/src/data/preprocessing/lagging_indicators/manufacture_inventory_sales_ratio.py",
    "/Users/pintoza/Desktop/dev/analytics-engineering/real-time-indicators/src/data/preprocessing/lagging_indicators/unit_labor_costs_all.py",
    "/Users/pintoza/Desktop/dev/analytics-engineering/real-time-indicators/src/data/preprocessing/leading_indicators/avg_consumer_expectations.py",
    "/Users/pintoza/Desktop/dev/analytics-engineering/real-time-indicators/src/data/preprocessing/leading_indicators/avg_weekly_hours_manufacture.py",
    "/Users/pintoza/Desktop/dev/analytics-engineering/real-time-indicators/src/data/preprocessing/leading_indicators/avg_weekly_initial_jobless_claims.py",
    "/Users/pintoza/Desktop/dev/analytics-engineering/real-time-indicators/src/data/preprocessing/leading_indicators/building_permits.py",
    "/Users/pintoza/Desktop/dev/analytics-engineering/real-time-indicators/src/data/preprocessing/leading_indicators/interest_rate_spread.py",
    "/Users/pintoza/Desktop/dev/analytics-engineering/real-time-indicators/src/data/preprocessing/leading_indicators/manufacture_new_order_capital.py",
    "/Users/pintoza/Desktop/dev/analytics-engineering/real-time-indicators/src/data/preprocessing/leading_indicators/manufacturer_new_orders_consumer.py",
    "/Users/pintoza/Desktop/dev/analytics-engineering/real-time-indicators/src/data/preprocessing/leading_indicators/sp_500_index.py",
]

# Execute preprocessing scripts
for script in preprocess_scripts:
    subprocess.run([python_interpreter, script], env=os.environ.copy())
    time.sleep(10)  # Adjust the sleep time as needed
