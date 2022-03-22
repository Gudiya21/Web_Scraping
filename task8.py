import requests
from bs4 import BeautifulSoup
import json
import os
from task1 import scraped_movie_details
caching=scraped_movie_details()
def cache_movie():
    for i in caching:
        url=("/home/admin123/Desktop/task8")+i["Name"]+".text"
        if os.path.exists(url):
            pass
        else:
            with open (("/home/admin123/Desktop/task8")+i["Name"]+".text","w") as f8:
                data=requests.get(i["URL"])
                m=f8.write(data.text)
cache_movie()