import json
from task2 import group_by_year
file =  open("task2.json","r")
data = json.load(file)
def decade_by_year():
    dict={}
    list=[]
    for i in data:
        modulus=int(i)%10
        decade=int(i)-modulus
        if decade not in list:
            list.append(decade)
    list.sort()
    for j in list:
        dict[j]=[]
    for j in dict:
        decade10=j+9
        for k in data:
            if int(k)<=decade10 and int(k)>=j:
                for l in data[k]:
                    dict[j].append(l)
    with open("task3.json","w+") as f4:
        json.dump(dict,f4,indent=4)
    return dict
decade_by_year()