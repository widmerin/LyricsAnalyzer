# Lyrics Analyzer

## Teammember
Michael Job & Ina Widmer

## Idee
Analyse the used words in chart songs.
Which words are used the most, in what year...
Are words like 'facebook' and so on since the rise of social media even present in chartsongs?


## Datenquellen
Die Hitparaden Lieder der letzten 20 Jahre werden von der Schweizer Hitparaden Seite bezogen.

Link: https://hitparade.ch/charts/singles/

Die Lyrics werden über die API lyrics.ovh geholt.  

Link: https://api.lyrics.ovh/

  
Zeitraum: 7.10.2018 - 20 Jahre zurück (Quartalsweise)   
Anz. Datensätze: Top 15 pro Datum (80 mal = 1200 Songs)

Um die Daten zu generieren muss das Pyhton Script ```charts.py``` ausgeführt werden

## Raw Data
Die Daten werden als JSON Objekte in einem  File gepeichert. 

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

