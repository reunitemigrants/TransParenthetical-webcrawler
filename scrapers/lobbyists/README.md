# Overview

## Setup
Install virtualenv and run: `pip install -U -r requirements.txt`

## Scripts

### pull_data.py
Pulls data from bulk CSV data fec.gov and saves the data onto local disk

### process_data.py
Processes the CSV data on local disk. Starts with a hard-coded list of committees and tracks which committees that committee contributed to. Unravels/untumbles the contributions to eventually get the candidates

#### Caveats
Not sure how to interpret the direction of the contribution listed here: https://www.fec.gov/campaign-finance-data/any-transaction-one-committee-another-file-description/