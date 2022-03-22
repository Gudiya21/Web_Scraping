from  task1 import scraped_movie_details
import json
file =  open("task1.json","r")
data = json.load(file)
def group_by_year():
    dic = {}
    for i in data:
        top_movie_list= []
        year = i["Year"]
        if year not in dic:
            for key in data:
                if year == key["Year"]:
                    top_movie_list.append(key)
            dic[year] = top_movie_list
    with open("task2.json","w+") as file:
        json.dump(dic,file,indent = 4)
        a = json.dumps(dic)
group_by_year()