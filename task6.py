from bs4 import BeautifulSoup
import requests
import json
file=open("task5.json","r+")
d=json.load(file)
def language_details():
    count={}
    for i in d:
        if "Language" in i:
            lang=i["Language"]
        for i in lang:
            if i not in count:
                count[i]=1
            else:
                count[i]+=1
    with open("task6.json","w+") as file6:
        json.dump(count,file6,indent=4)
language_details()