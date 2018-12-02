# Web Scraper for County Meeting Minutes

## Installation

```
$> pip -r requirements.txt`
```

## Getting Started

After installing dependencies, run the main crawler script:
```
$> python3 crawl_minutes.py
```
- This should trigger the crawling of different county meeting notes. See `sources.json` for configuration of more county websites.
- Each county's meeting notes (PDF) is downloaded, converted into plaintext, and matched on keywords. See `get_words.py` for details on parsing the PDF into a list of existing keywords. See `words.py` for the keywords we're matching on.
- After each minutes file is downloaded, parsed and matched, a final output CSV file is written `rumor_proposals.csv` .

## Next Steps

- We still need to parse the `DATE`and `BLOB_TEXT` parts for the CSV output.
- We still need to integrate the output `rumor_proposals.csv` with the main frontend application.


### Notes

> Should read write files to a temporary directory rather than main or pass filestream through. Look to expanding keyword dictionary and perhaps comparing document score against keywords rather than looking for occurance.
> - @3dprintscanner (Anthony)

> I'm sorry in advance for my code-- I very rarely write python! :(. Delete and rewrite everything at-will!
> - @harrytruong (Harry)
