# Lyrics Analyzer
## Idee
Analyse used words in Songs ??

## Datenquellen
Die Hitparaden Lieder der letzten 20 Jahre werden von der Schweizer Hitparaden Seite https://hitparade.ch/charts/singles/ bezogen.
Die Lyrics werden über die API https://api.lyrics.ovh/ geholt.  

  
Zeitraum: 7.10.2018 - 20 Jahre zurück (Quartalsweise)
Anz. Datensätze: Top 15 pro Datum (80 mal = 1200 Songs)

Um die Daten zu generien muss das Pyhton Script ```charts.py``` ausgeführt werden

## Raw Data
Die Daten werden als Objekte in einem JSON abgelegt. 

```
[{   
    "artist": "Calvin Harris & Sam Smith",  // Song interpret
    "title": "Promises",                    // Song title
    "date": "07-10-2018",                   // Charts Date
    "ranking": "3",                         // Charts Ranking
    "lyrics": "Are you drunk enough? ..."   // Lyrics
}, ... ]

