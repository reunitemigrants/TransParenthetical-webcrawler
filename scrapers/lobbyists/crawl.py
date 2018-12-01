# built-in modules
import csv
import io
import zipfile

# 3rd party modules
import requests

# https://www.fec.gov/data/advanced/?tab=bulk-data
BASE_CANDIDATES_URL = "https://www.fec.gov/files/bulk-downloads/20%(year)s/cn%(year)s.zip"
BASE_COMMITTEES_URL = "https://www.fec.gov/files/bulk-downloads/20%(year)s/cm%(year)s.zip"
BASE_LINKAGES_URL = "https://www.fec.gov/files/bulk-downloads/20%(year)s/ccl%(year)s.zip"
BASE_CONTRIBUTIONS_URL = "https://www.fec.gov/files/bulk-downloads/20%(year)s/pas2%(year)s.zip"

# The year to pull data from. Seems like years are always even
YEAR = "18"


# get_url generates a URL using the given base URL and year
def get_url(base_url, year):
    return base_url % {"year": year}


# extract_remote_csv fetches the CSV file specified by the url, extracts the contents, parses the CSV
# and returns a list of the data
def extract_remote_csv(url):
    resp = requests.get(url, stream=True)
    resp.raise_for_status()

    f = io.BytesIO()
    for c in resp.iter_content(None):
        f.write(c)

    with zipfile.ZipFile(f) as zf:
        filenames = zf.namelist()
        if len(filenames) != 1:
            raise RuntimeError("Expected a single file in the zip file. Got: %s" % filenames)
        filename = filenames[0]
        # import ipdb; ipdb.set_trace()
        with zf.open(filename) as unzipped:
            rows = csv.reader(io.TextIOWrapper(unzipped))
            return [r for r in rows]

    return []

def main():
    candidates = extract_remote_csv(get_url(BASE_CANDIDATES_URL, YEAR))
    print("Candidates:", candidates[:3])
    committees = extract_remote_csv(get_url(BASE_COMMITTEES_URL, YEAR))
    print("Committees:", committees[:3])
    linkages = extract_remote_csv(get_url(BASE_LINKAGES_URL, YEAR))
    print("Linkages:", linkages[:3])
    contributions = extract_remote_csv(get_url(BASE_CONTRIBUTIONS_URL, YEAR))
    print("Contributions:", contributions[:3])


if __name__ == "__main__":
    main()
