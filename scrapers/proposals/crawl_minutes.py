import requests
import csv
import re
import download

# TODO: import this config from a CSV file:
# location,minutes_url,minutes_regex
sources = [
    ["Jerome County, Idaho",
    "https://www.jeromecountyid.us/AgendaCenter/",
    "<td class=\"minutes\".+href=\"/AgendaCenter/(.+?)\".+<\/a>"],

    ["Charlton County, Georgia",
    "https://charltoncountyga.us/AgendaCenter/",
    "<td class=\"minutes\".+href=\"/AgendaCenter/(.+?)\".+<\/a>"]
]


with open('rumor_proposals.csv', mode='w') as proposals_file:

    csvwriter = csv.writer(proposals_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    csvwriter.writerow(["date", "type", "url", "location", "text"])

    for [location, minutesUrl, minutesRegex] in sources:
        ## minutesUrl = 'https://charltoncountyga.us/AgendaCenter/'
        ## minutesRegex = '<td class="minutes".+href="/AgendaCenter/(.+?)".+<\/a>'

        r = requests.get(minutesUrl, verify=False)
        p = re.compile(minutesRegex)

        for minute in p.findall(r.text):
            targetUrl = minutesUrl + minute
            # print(targetUrl)

            targetReq = requests.get(targetUrl, verify=False)

            with open('target.pdf', 'wb') as ff:
                ff.write(targetReq.content)

            pdf = download.convert_pdf_to_txt('target.pdf')
            print(pdf)

            # # TODO: make call to determine if PDF contains relevant keywords
            relevant = True

            if relevant:
                csvwriter.writerow(['DATE', 'proposals', targetUrl, location, 'BLOB_TEXT'])
