# TransParenthetical-webcrawler

We want to build a crawler that looks for detention center proposals or permit applications and then alerts the communities involved. Outcomes would include an email and SMS alert system, a website or app that provides a feed of these alerts, and finally a means for the public to contact their officials with concerns.

For more details, see this Google Doc: 
https://docs.google.com/document/d/1nQJqXpaL-jEzYg8nJR5xBL1z1MzwaIFWOehkiGVQMVo


MVP Architecture | Future Architecture 
------- | -------
For this **MVP**, we're focused only on building an Alert Feed website that scrapes for "rumored" detention centers based on a few key source types: **Lobbyists**, **Media**, **Permits**, **Proposals** | ![Overview](https://lh4.googleusercontent.com/cWoyzMh31gmjKAB5CUfWyoR23wXuKW0J5p6P9A8rVXA2yj64f6agDEDYxzG9-QTb0Io2xRZnc3Vk1rotlIAHLTRPI92aLpEm-Hqv9e--yezjrebEBEAC6MS8-aequkpNURtEvvg)

Sources Types | Description
----- | -----
Lobbyists | Lobbying groups for detention centers (e.g., GEOGroup, CoreCivic) are contributing campaign funds to different candiates. We can crawl campaign contribution datasets to predict which locations they're focusing on, and trigger alerts about potential future detention centers.
Media | News articles are being published in local communities to notify and discuss creation of detention centers. We can crawl news articles to trigger alerts when relevant keywords are mentioned.  
Permits | In the process of creating detention centers, we imagine companies will require construction permits. We can crawl construction permit datasets to trigger alerts when new construction is starting.
Proposals | In the process of creating detention centers, we imagine local county meetings have mentions of creating detention centers. We can crawl meeting notes to trigger alerts when relevant keywords are mentioned.

Mobile Mock | Desktop Mock (courtesy of @holly!)
----- | -----
![mobile mock](https://raw.githubusercontent.com/reunitemigrants/TransParenthetical-webcrawler/master/mocks/alert_feed__expanded_.png) | ![desktop mock](https://raw.githubusercontent.com/reunitemigrants/TransParenthetical-webcrawler/master/mocks/desktop_hd.png)

----

### Project Structure

See subdirectory README.md for each component for more details.
```
/alert-feed      - main frontend application
/scrapers        - collection of data source scrapers
  /lobbyists       - status: scraping data, not yet writing to CSV
  /media           - status: no progress
  /permits         - status: no progress
  /proposals       - status: scraping data, writing to CSV
```

Each scraper is focused on generating CSV file feeds for each source, with the following headers: `DATE, SOURCE_TYPE, URL, LOCATION, BLOB_TEXT`. The ultimate goal is to combine each scraper's output w/ the frontend interface.


### Next Steps

- `/alert-feed` needs to connect with actual CSV outputs
- `/lobbyists` needs to write relevant contributions to CSV files
- `/proposals` needs to connect CSV output to main frontend app
