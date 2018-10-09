from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import requests
import json

#  Collect swiss charts data
#  From current date 7.10.2018) until ??
#  Save Data as json: Song | Artist | Date | Ranking

data = []          # list of fetched data

# Get Charts data for given date
def getChartsData(date, limit):
    page = requests.get('https://hitparade.ch/charts/singles/'+date)

    # Find all Links with artist and song information
    # <a class="navb" href="/song/Imagine-Dragons/Zero-1796671" style="text-decoration:none;"><b>Imagine Dragons</b><br/>Zero</a>
    soup = BeautifulSoup(page.content, 'html.parser')
    links = soup.findAll("a", {"class": "navb"})


    for i in range(limit):
        artist = links[i].find("b").getText()
        song = links[i].find('br').nextSibling
        print(str(i + 1) + ". " + artist + " - " + str(song))
        # Get Lyrcs for song with api.lyrics.ovh
        lyrics = getLyrics(artist,song)

        # If no lyrcs was found try with suggest Request
        if len(lyrics) == 0:
            req = requests.get('https://api.lyrics.ovh/suggest/' + song + " " + artist)

            # Get Lyrcs for song
            if (req.status_code == 200 and json.loads(req.content)["data"]):
                # Get artist and Song from first title
                artist = json.loads(req.content)["data"][0]["artist"]["name"]
                song = json.loads(req.content)["data"][0]["title"]
                lyrics = getLyrics(artist, song)

        if len(lyrics) > 0:
            data.append({"artist": artist, "title": song, "date": date, "ranking": str(i + 1), "lyrics": lyrics})
        else:
           print(" No lyrics was found https://api.lyrics.ovh/suggest/" + song + " " + artist)

def getLyrics(artist, song):
    lyrics = ""
    req = requests.get('https://api.lyrics.ovh/v1/' + artist + '/' + song)

    if(req.status_code == 200):
        # Decode and save lyrics content
        lyrics = json.loads(req.content.decode('utf-8'))['lyrics']
        lyrics = lyrics.replace('\r', '')

    return lyrics


def main():
    charts_date = datetime(2018,10,7) # Startdate
    fetch_dateS = datetime.now().strftime("%d-%m-%Y")

    records = 1        # how many records should be saved
    limit = 15         # songs per charts
    daysdelta = 28     # 28=month, 7=week   inbetween charts


    for i in range(records):
        print("Charts: "+charts_date.strftime("%d.%m.%Y"))
        getChartsData(charts_date.strftime("%d-%m-%Y"), limit)
        charts_date = charts_date - timedelta(days=daysdelta)  # get date from daysdelta before

    print(data)
    with open('data/data-'+fetch_dateS+'.json', 'w') as outfile:
        json.dump(data, outfile)



if __name__ == '__main__':
  main()