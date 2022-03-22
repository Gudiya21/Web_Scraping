import json
with open("task5.json","r+")as file:
    ld=json.load(file)
def analyse_language_and_directors():
    dic={}
    list=[]
    for i in ld:
        for j in i["Director"]:
            if j not in list:
                list.append(j)
    for k in list:
        dic1={}
        for l in ld:
            if k in l["Director"]:
                if "Language" in l:
                    a=l["Language"]
                    for g in a:                       
                        if g  in  dic1:
                            dic1[g]=dic1[g]+1
                        if g not in dic1:
                            dic1[g]=1
                    dic[k]=dic1
    with open("task10.json","w+") as f10:
        json.dump(dic,f10,indent=4)
        return dic
analyse_language_and_directors()