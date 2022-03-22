from bs4 import BeautifulSoup
import json
import requests 
url="https://www.rottentomatoes.com/top/bestofrt/top_100_animation_movies/"
response=requests.get(url)
soup=BeautifulSoup(response.text,"html.parser")
def scraped_movie_details():
    maindiv=soup.find("div",class_="panel-body content_body allow-overflow")
    table=maindiv.find("table",class_="table")
    trs=table.find_all("tr")
    l=[]
    for i in trs:
        td=i.find_all("td")
        dic={}
        for j in td:
            rank=i.find("td","bold").get_text()[:-1]
            dic["Rank"]=int(rank)
            rating=i.find("span",class_="tMeterScore").get_text()[1:3]
            dic["Rating"]=float(rating)
            name=i.find("a",class_="unstyled articleLink")["href"][3:]
            dic["Name"]=name
            reviews=i.find("td",class_="right hidden-xs").get_text()
            dic["Reviews"]=int(reviews)
            year=i.find("a",class_="unstyled articleLink").get_text()[-5:-1]
            dic["Year"]=int(year)
            url=i.find("a",class_="unstyled articleLink")["href"]
            link="https://www.rottentomatoes.com/"+url
            dic["URL"]=link
        l.append(dic)
    if {} in l:
        l.remove({})
    with open("task1.json","w") as f:
        json.dump(l,f,indent=1)
        return l   
        
scraped_movie_details()