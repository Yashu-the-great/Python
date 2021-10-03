from bs4 import BeautifulSoup
import requests


def get(city:str):
    # this functions fetches and returns the data in the form of [time, sky_conditions, temp] 
    soup = BeautifulSoup(requests.get("https://www.google.com/search?q="+"weather"+city).content, 'html.parser')
    data = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text.split("\n")
    return [data[0],data[1],soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text]

if __name__ == "__main__":
    print(get("lucknow"))