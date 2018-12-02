# built-in modules
import collections
import csv
import io
import zipfile

# local modules
import constants

# The committee ids. Can be found in the constants.COMMITTEES_FILENAME CSV file
PAC_IDS = {
    "C00208322",  # MANAGEMENT AND TRAINING CORPORATION POLITICAL ACTION COMMITTEE
    "C00366468",  # CORECIVIC, INC. POLITICAL ACTION COMMITTEE
    "C00382150",  # THE GEO GROUP, INC. POLITICAL ACTION COMMITTEE
}


# Processes the CSV file specified by the given name and returns the contents (Python list)
def extract_csv(filename):
    with zipfile.ZipFile(filename) as zf:
        filenames = zf.namelist()
        if len(filenames) != 1:
            raise RuntimeError("Expected a single file in the zip file. Got: %s" % filenames)
        filename = filenames[0]
        with zf.open(filename) as unzipped:
            unzipped_txt = io.TextIOWrapper(unzipped)  # convert bytes to text for CSV processing
            # sniff the CSV to determine the delimiter
            dialect = csv.Sniffer().sniff(unzipped_txt.read(2048), delimiters="|")
            unzipped_txt.seek(0)
            # Can't return a generator since the file will be closed by the context manager
            rows = csv.reader(unzipped_txt, dialect=dialect)
            return [r for r in rows]

    return []


# untumble_committees goes through cross comittee transactions (committee_map)
def untumble_committees(committee_map, init_committee_ids):
    committee_ids = set()
    ids_to_process = collections.deque(init_committee_ids)

    while len(ids_to_process):
        cid = ids_to_process.pop()
        if cid in committee_ids:
            continue
        committee_ids.add(cid)
        ids_to_process.extend(committee_map[cid])

    return committee_ids


def main():
    # Not fetching linkages since they don't seem to properly link candidates and committees
    # columns described here: https://www.fec.gov/campaign-finance-data/candidate-committee-linkage-file-description/
    # linkages = extract_csv(constants.LINKAGES_FILENAME)
    # print("# Linkages:", len(linkages))
    # print("Sample Linkages:", linkages[:3])

    # columns described here: https://www.fec.gov/campaign-finance-data/any-transaction-one-committee-another-file-description/
    committee_map = collections.defaultdict(list)
    for r in extract_csv(constants.CROSS_COMMITTEE_TRANSACTIONS_FILENAME):
        committee_map[r[0]].append(r[15])
        committee_map[r[15]].append(r[0])

    committee_ids = untumble_committees(committee_map, PAC_IDS)
    # columns described here: https://www.fec.gov/campaign-finance-data/committee-master-file-description/
    committees = [r for r in extract_csv(constants.COMMITTEES_FILENAME)
                  if r[0] in committee_ids]
    print("# Committees:", len(committees))
    print("Sample Committees:", committees[:3])

    # columns described here: https://www.fec.gov/campaign-finance-data/contributions-committees-candidates-file-description/
    contributions = [r for r in extract_csv(constants.CONTRIBUTIONS_FILENAME) if r[0] in committee_ids]
    candidate_ids = {c[15] for c in contributions}
    print("# Contributions:", len(contributions))
    print("Sample Contributions:", contributions[:3])

    # columns described here: https://www.fec.gov/campaign-finance-data/candidate-master-file-description/
    candidates = [r for r in extract_csv(constants.CANDIDATES_FILENAME) if r[0] in candidate_ids]
    print("# Candidates:", len(candidates))
    print("Sample Candidates:", candidates[:3])

    # TODO: create alerts on new candidates or new contributions to candidates


if __name__ == "__main__":
    main()
