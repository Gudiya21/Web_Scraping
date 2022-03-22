from bs4 import BeautifulSoup
import requests
import json
file=open("task5.json","r+")
d=json.load(file)
def analyse_movies_genre():
    count={}
    for i in d:
        if "Genre" in i:
            direct=i["Genre"]
        for i in direct:
            if i not in count:
                count[i]=1
            else:
                count[i]+=1
    with open("task11.json","w+") as file11:
        json.dump(count,file11,indent=4)
    return count
analyse_movies_genre()