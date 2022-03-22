import requests
from bs4 import BeautifulSoup
import json,random,time
import os
from task1 import scraped_movie_details
caching=scraped_movie_details()
def time_sleep():
    for i in caching:
        random_time=random.randint(1,3)
        url=("/home/admin123/Desktop/task9")+i["Name"]+".json"
        if os.path.exists(url):
            pass
        else:
            with open (("/home/admin123/Desktop/task9")+i["Name"]+".json","w") as f8:
                data=requests.get(i["URL"])
                m=f8.write(data.text)
        time.sleep(random_time)
time_sleep()