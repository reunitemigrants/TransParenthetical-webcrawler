# Overview

## Setup
1. Install virtualenv
1. Create a virtual environment: `virtualenv venv`
    * If Python 3 isn't the default for your system, use: `virtualenv -p python3 venv`
1. Activate the virtual environment: `. venv/bin/activate`
    * The virtual environment needs to be active when running any of the scripts
1. Install dependencies: `pip install -U -r requirements.txt`

## Scripts

### pull_data.py
Pulls data from bulk CSV data fec.gov and saves the data onto local disk

### process_data.py
Processes the CSV data on local disk. Starts with a hard-coded list of committees and tracks which committees that committee contributed to. Unravels/untumbles the contributions to eventually get the candidates

#### Caveats
Not sure how to interpret the direction of the contribution listed here: https://www.fec.gov/campaign-finance-data/any-transaction-one-committee-another-file-description/