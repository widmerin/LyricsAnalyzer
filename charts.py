from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import requests
import json

#  Collect swiss charts data
#  From current date until ??
#  Save Data as: Song | Artist | Date | Ranking

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

        #print(str(i + 1) + ". " + artist + " - " + str(song))
        data.append([artist, str(song), date, str(i + 1)])



def main():
    charts_date = datetime.now() # Startdate .now()
    fetch_dateS = charts_date.strftime("%d-%m-%Y")

    records = 3        # how many records should be saved
    limit = 15         # songs per charts
    daysdelta = 30     # 30=month, 7=week   inbetween charts


    for i in range(records):
        print("Charts: "+charts_date.strftime("%d.%m.%Y"))

        getChartsData(charts_date.strftime("%d-%m-%Y"), limit)
        charts_date = charts_date - timedelta(days=daysdelta)  # get date from daysdelta before

    print(data);
    with open('data/data-'+fetch_dateS+'.json', 'w') as outfile:
        json.dump(data, outfile)



if __name__ == '__main__':
  main()