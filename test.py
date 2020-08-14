import mysql
import json
import requests as r 
import pickle
import time

with open("aland_links.pkl", "rb") as f:
    aland_links = pickle.load(f)
title_list = []
count = 0
for a in aland_links:

    loop_breaker = 429
    while loop_breaker == 429:
        response = r.get(a)
        loop_breaker = response.status_code
        if loop_breaker == 429:
            print("429 - Too many requests in too short timeframe. Please try again later.")
            print("going to sleep...")
            print("By the way, {} out of {} so far.".format(count, len(aland_links)))
            time.sleep(5)
            print("zzz...")
            time.sleep(5)
            print("woke up!")
    if response.status_code == 404:
        print("did not find " + a)
    elif response.status_code == 200:
        j = json.loads(response.text)
        title_list.append(j["title"])
        count = count + 1
for t in title_list:
    print(t + "\n")
print(len(aland_links))