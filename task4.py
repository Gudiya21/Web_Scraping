from task1 import scraped_movie_details
import requests
from bs4 import BeautifulSoup
import json
def first_movie(data1):
    url=requests.get(data1)
    url_details = BeautifulSoup(url.text,"html.parser")
    li=url_details.find_all('li',class_="meta-row clearfix")
    name=url_details.find("h1",class_="scoreboard__title").get_text()
    details={}
    list=[]
    movie=scraped_movie_details()
    for i in li:
        k=i.text
        n=k.split()
        for j in n:
            if "Rating" in j:
                details["name"]=name
                details["Rating"]=n[1]
            if "Genre" in j:
                a=n[1:]
                m=" "
                for i in a:
                    m+=i
                m=m.split(",")
                details["Genre"]=m
            if "Language" in j:
                details["Language"]=n[2:]
            if "Director" in j:
                a=n[1:]
                s=" "
                for i in a:
                    s+=i
                s=s.split(",")
                details["Director"]=s
            if "Producer" in j:
                a=n[1:]
                l=" "
                for i in a:
                    l+=i
                l=l.split(",")
                details["Producer"]=l
            if "Writer" in j:
                a=n[1:]
                v=" "
                for i in a:
                    v+=i
                v=v.split(",")
                details["Writer"]=v
            if "Release" in j:
                details["Release"]=n[3:6]
            if "Runtime" in j:
                time=n[1:]
                i=0
                while i<len(time):
                    hour=time[0][0]
                    mint=time[1]
                    min=mint[:-1]
                    i=i+1
                tom=int(hour)*60+int(min)
                details["Runtime"]=tom
    with open("task4.json","w+")as file:
        json.dump(details,file,indent=4)
        return details
first_movie("https://www.rottentomatoes.com/m/toy_story_4")