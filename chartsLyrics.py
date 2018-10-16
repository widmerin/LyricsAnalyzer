from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import requests
import json

#  Collect swiss charts data
#  From 7.10.2018 until 4.10.1998

data = []  # list of fetched data


# Get Charts data for given date
def getChartsData(date, limit):
    page = requests.get('https://hitparade.ch/charts/singles/' + date)

    # Find all Links with artist and song information
    soup = BeautifulSoup(page.content, 'html.parser')
    links = soup.findAll("a", {"class": "navb"})

    # Get lyrics for each song
    for i in range(limit):
        artist = links[i].find("b").getText()
        song = links[i].find('br').nextSibling
        print(str(i + 1) + ". " + artist + " - " + str(song))

        # Get Lyrics for song from api.lyrics.ovh
        [status, lyrics] = getLyrics(artist, song)

        # If no lyrcs was found try with suggest request
        if (status != 200):
            req = requests.get('https://api.lyrics.ovh/suggest/' + song + " " + artist)

            # Get Lyrcs for song
            if (req.status_code == 200 and json.loads(req.content)["data"]):
                artist = json.loads(req.content)["data"][0]["artist"]["name"]
                song = json.loads(req.content)["data"][0]["title"]
                [status, lyrics] = getLyrics(artist, song)

        # Create json object
        data.append({"artist": artist, "title": song, "date": date, "ranking": str(i + 1), "lyrics": lyrics})

        if (len(lyrics) == 0):
            print(" No lyrics was found https://api.lyrics.ovh/suggest/" + song + " " + artist)


def getLyrics(artist, song):
    lyrics = ""
    req = requests.get('https://api.lyrics.ovh/v1/' + artist + '/' + song)
    status = req.status_code

    if (status == 200):
        # Decode and save lyrics content
        lyrics = json.loads(req.content.decode('utf-8'))['lyrics']
        lyrics = lyrics.replace('\r', '')

    return status, lyrics


def main():
    charts_date = datetime(2018, 10, 7)  # Startdate
    fetch_dateS = charts_date.now().strftime("%d-%m-%Y")

    records = 88  # how many records should be saved (88 = 20 years 4.10.1998)
    limit = 25  # songs per charts
    daysdelta = 84  # 84 = quarter(12 weeks), days in between charts

    for i in range(records):
        print("Charts: " + charts_date.strftime("%d.%m.%Y"))
        getChartsData(charts_date.strftime("%d-%m-%Y"), limit)
        charts_date = charts_date - timedelta(days=daysdelta)  # get date from daysdelta before

    print(data)
    with open('data/data-' + fetch_dateS + '.json', 'w') as outfile:
        json.dump(data, outfile)


if __name__ == '__main__':
    main()
