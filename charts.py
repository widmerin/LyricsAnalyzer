from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import requests

#  Collect swiss charts data
#  From current date 30.09.2018 until ??
#  Save Data as: Song | Artist| Date | Ranking

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
        ## ToDo: Save artist, song, date and ranking in List?

def main():
    charts_date = datetime(2018, 9, 30) # Startdate

    weeks = 25  # how many weeks should be saved
    limit = 15  # songs per charts


    for i in range(weeks):
        print("Charts: "+charts_date.strftime("%d.%m.%Y"))

        getChartsData(charts_date.strftime("%d-%m-%Y"), limit)
        charts_date = charts_date - timedelta(days=7) # get date from week before

if __name__ == '__main__':
  main()