import mysql
import json
import requests as r 
import pickle
import time


def region_finder(api_json,link):
    contains_aland = False
    for l in api_json["variables"]:
        for k in l.keys():
            print(k)
            if k == "valueTexts":
                print(l[k])
                for le in l[k]:
                    if ("Åland" in le) or ("Eckerö" in le):
                        contains_aland = True
    print(link +" "+ str(contains_aland))
    return contains_aland

with open("api_links.pkl", "rb") as f:
    api_links = pickle.load(f)
region_links = []
count = 0
count_total = 0
list_length = len(api_links)
for a in api_links:
    count_total = count_total +1
    loop_breaker = 429
    while loop_breaker == 429:
        response = r.get(a)
        loop_breaker = response.status_code
        if loop_breaker == 429:
            print("429 - Too many requests in too short timeframe. Please try again later.")
            print("going to sleep...")
            print("By the way, {} out of {} out of {} so far.".format(count, count_total, list_length ))
            time.sleep(5)
            print("zzz...")
            time.sleep(5)
            print("woke up!")
    if response.status_code == 404:
        print("did not find " + a)
    elif response.status_code == 200:
        j = json.loads(response.text)
        if region_finder(j,a):
            region_links.append(a)
            count = count +1
            print("Succesfully added {} links out of {}!".format(count, count_total))
for r in region_links:
    print(r)
with open("aland_links.pkl","wb") as g:
    pickle.dump(region_links,g)




