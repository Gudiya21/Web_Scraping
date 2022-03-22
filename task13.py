from bs4 import BeautifulSoup
import json
import requests
from task4 import first_movie
from task12 import scrape_movie_cast
def scrape_movie_all(url):
    l=[]
    t4=first_movie(url)
    t12=scrape_movie_cast(url)
    l.append(t4)
    l.append(t12)
    with open("task13.json","w+") as f12:
        json.dump(l,f12,indent=4)
        return l
scrape_movie_all("https://www.rottentomatoes.com/m/toy_story_4")
# 267861