import requests
import csv
import re
import get_words
import words
import json
# TODO: import this config from a CSV file:
# location,minutes_url,minutes_regex

jt = open('sources.json')
sources = json.loads(jt.read())
jt.close()

with open('rumor_proposals.csv', mode='w') as proposals_file:

    csvwriter = csv.writer(proposals_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    csvwriter.writerow(["date", "type", "url", "location", "text"])

    for [location, minutesUrl, minutesRegex] in sources:
        ## minutesUrl = 'https://charltoncountyga.us/AgendaCenter/'
        ## minutesRegex = '<td class="minutes".+href="/AgendaCenter/(.+?)".+<\/ajt

        r = requests.get(minutesUrl, verify=False)
        p = re.compile(minutesRegex)

        for minute in p.findall(r.text):
            targetUrl = minutesUrl + minute
            # print(targetUrl)

            targetReq = requests.get(targetUrl, verify=False)

            with open('target.pdf', 'wb') as ff:
                ff.write(targetReq.content)

            keywords = get_words.get_keywords_from_file('target.pdf')
            

            # # TODO: make call to determine if PDF contains relevant keywords
            relevant = words.contains_keywords(keywords)

            if relevant:
                csvwriter.writerow(['DATE', 'proposals', targetUrl, location, 'BLOB_TEXT'])
