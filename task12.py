import requests
import json 
from bs4 import BeautifulSoup

def scrape_movie_cast(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"html.parser")
    list=[]
    dic={}
    maindiv=soup.find("div",class_="castSection")
    div=maindiv.find_all("div",class_="cast-item media inlineBlock")
    div2=maindiv.find_all("div",class_="cast-item media inlineBlock moreCasts hide")
    for i in div:
        dic={}
        cast=i.find("a")["href"][11:]
        dic["Name"]=cast
        list.append(dic)
 
    for j in div2:
        dic={}
        cast2=j.find("a")["href"][11:]
        dic["Name"]=cast2
        list.append(dic)
    with open("task12.json","w+") as f12:
        json.dump(list,f12,indent=4)
        return list
scrape_movie_cast("https://www.rottentomatoes.com/m/toy_story_4")


