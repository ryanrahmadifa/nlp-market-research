import requests
from bs4 import BeautifulSoup
from datetime import datetime
import numpy as np
import pandas as pd

def get_url(name):
    url_template="https://news.google.com/search?q=mobil%20listrik&hl=en-ID&gl=ID&ceid=ID%3Aen"
    url = url_template.format(name)
    return url

def get_articles(url):
    articles = []
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    results = soup.find_all('h3', {'class':'DY5T1d RZIKme'})
    for item in results:
        try:
            title = item.find('a').text
            link = item.find('a')['href']
            source = item.find('a')['aria-label']
            date = item.find('time')['datetime'][0:10]
            articles.append({'title':title, 'date':date, 'source':source, 'link':link})
        except:
            continue
    return articles

X = []
X.append(get_articles("https://news.google.com/search?q=mobil%20listrik&hl=en-ID&gl=ID&ceid=ID%3Aen"))

print(X)

