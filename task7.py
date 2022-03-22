from bs4 import BeautifulSoup
import requests
import json
file=open("task5.json","r+")
d=json.load(file)
def director_details():
    count={}
    for i in d:
        if "Director" in i:
            direct=i["Director"]
        for i in direct:
            if i not in count:
                count[i]=1
            else:
                count[i]+=1
    with open("task7.json","w+") as file7:
        json.dump(count,file7,indent=4)
    return count
director_details()