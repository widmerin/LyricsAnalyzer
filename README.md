# Lyrics Analyzer
## Idea
Analyse the words used in chartsongs.
Which words are used the most, in what year...
Are words like 'facebook' and so on since the rise of social media present in chartsongs?

## Datasource
Chartsongs of the last 20 years are gathered from swiss charts website. There is no API provided, so we used webcrawling.

Link: https://hitparade.ch/charts/singles

Lyrics are collected over the API lyrics.ovh.  

Link: https://api.lyrics.ovh

### Parameters  
Time range: from 4.10.1998 to 7.10.2018
Time slot: every three months (every 84 days)
Songs: Top 25 songs per date

### Fetching the data
Fetch Date: 15.10.2018 20:02  
Fetched data items: 2200  
  
Run Pyhton Script ```chartsLyrics.py``` to fetch data again and save to JSON file.

### Raw Data
The gathered data is stored as a JSON file.  

Record sample:
```
[{   
    "artist": "Calvin Harris & Sam Smith",  // Song interpret
    "title": "Promises",                    // Song title
    "date": "07-10-2018",                   // Charts Date
    "ranking": "3",                         // Charts Ranking
    "lyrics": "Are you drunk enough? ..."   // Lyrics
 }, 
    ...
 ]
```  

#### Projectinfo
@author: Ina Widmer, Michael Job  
Module: dsp Data science with Python  
FHNW iCompetence HS18
