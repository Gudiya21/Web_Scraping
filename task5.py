import json
from bs4 import BeautifulSoup
from task1 import scraped_movie_details
from task4 import first_movie
movies = scraped_movie_details()
def get_movie_details():  
    movie_list = []
    for i in movies:
        url1=i["URL"]
        # print(url1)
        a=first_movie(url1)
        movie_list.append(a)
        # print(movie_list)
    with open("task5.json","w+") as file5:
        json.dump(movie_list,file5,indent=4)
    return movie_list
get_movie_details()