# Lyrics Analyzer
@author: Ina Widmer, Michael Job  
Jan.2019
## Idea
Analyse the words used in chartsongs.
Which words are used the most, in what year...
Are words like 'facebook' and so on since the rise of social media present in chartsongs?
## Datasources
Chartsongs of the last 20 years are gathered from swiss charts website https://hitparade.ch/charts/singles . The lyrics were collected over the API lyrics.ovh. 
 
There is no API provided for the swiss charts data, so we used webcrawling. The crawler called for each required chartsdate the hitparade.ch website for the specific date  
Example: https://hitparade.ch/charts/singles/16-09-2018

The crawler got the artist and songtitle information from links with the css class `navb`   
For all collected charts songs the lyrics were collected over the API https://api.lyrics.ovh
### Parameters  
Time range: from 4.10.1998 to 7.10.2018  
Time slot: every three months (every 84 days)  
Songs: Top 25 songs per date
### Fetching the data
Fetch Date: 15.10.2018 20:02  
Fetched data items: 2200  
Fetched by: Ina Widmer, Michael Job 
  
Run Pyhton Script ```DataFetching.py``` or import Module and run ```DataFetching.loadData()``` to fetch data again and save to JSON file. 
### Raw Data
The gathered data is stored as a JSON file. The data are not filtered. Duplicate songs / lyrics are possible, if no lyrics was found for a song the lyrics attribute is empty.  
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
#### DataStory Presentation
###### to view DataStorySlides.ipynb as a Presentation run:
```
jupyter nbconvert DataStorySlides.ipynb --to slides --post serve
```
this will serve the slides at http://127.0.0.1:8000/DataStorySlides.slides.html

#### Projectinfo
Module: dsp Data science with Python  
FHNW iCompetence HS18
