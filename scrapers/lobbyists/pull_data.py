# 3rd party modules
import requests

# local modules
import constants

# https://www.fec.gov/data/advanced/?tab=bulk-data
BASE_CANDIDATES_URL = "https://www.fec.gov/files/bulk-downloads/20%(year)s/cn%(year)s.zip"
BASE_COMMITTEES_URL = "https://www.fec.gov/files/bulk-downloads/20%(year)s/cm%(year)s.zip"
BASE_LINKAGES_URL = "https://www.fec.gov/files/bulk-downloads/20%(year)s/ccl%(year)s.zip"
BASE_CONTRIBUTIONS_URL = "https://www.fec.gov/files/bulk-downloads/20%(year)s/pas2%(year)s.zip"
BASE_CROSS_COMMITTEE_TRANSACTIONS_URL = "https://www.fec.gov/files/bulk-downloads/20%(year)s/oth%(year)s.zip"


# get_url generates a URL using the given base URL and year
def get_url(base_url, year):
    return base_url % {"year": year}


# pull_remote_csv fetches the CSV file specified by the URL and saves it to the given filename
def pull_remote_csv(url, filename):
    print("fetching", url)
    resp = requests.get(url, stream=True)
    resp.raise_for_status()

    print("writing", filename)
    with open(filename, "wb") as f:
        for c in resp.iter_content(None):
            f.write(c)
    print("wrote", filename)


def main():
    pull_remote_csv(get_url(BASE_COMMITTEES_URL, constants.YEAR), constants.COMMITTEES_FILENAME)
    pull_remote_csv(get_url(BASE_CROSS_COMMITTEE_TRANSACTIONS_URL, constants.YEAR), constants.CROSS_COMMITTEE_TRANSACTIONS_FILENAME)
    pull_remote_csv(get_url(BASE_LINKAGES_URL, constants.YEAR), constants.LINKAGES_FILENAME)
    pull_remote_csv(get_url(BASE_CONTRIBUTIONS_URL, constants.YEAR), constants.CONTRIBUTIONS_FILENAME)
    pull_remote_csv(get_url(BASE_CANDIDATES_URL, constants.YEAR), constants.CANDIDATES_FILENAME)


if __name__ == "__main__":
    main()
