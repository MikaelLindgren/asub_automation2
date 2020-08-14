
import requests as r
import json
import time
import pickle
import region_check
base_dir = "http://pxnet2.stat.fi/PXWeb/api/v1/sv/StatFin"
buffer = []
def update_buffer(new_entry):
    buffer.append(new_entry)
    print(len(buffer))
def crawl(base_dir):
    if base_dir.endswith(".px"):
        update_buffer(base_dir)
        print(base_dir + " ends with .px")
    else:
        loop_breaker = 429
        while (loop_breaker == 429):
            response = r.get(base_dir)
            loop_breaker = response.status_code
            if loop_breaker == 429:
                print("429 - Too many requests in too short timeframe. Please try again later.")
                print("going to sleep...")
                time.sleep(5)
                print("zzz...")
                time.sleep(5)
                print("zzz...")
                time.sleep(5)
                print("woke up!")
        if response.status_code == 404:
            print("did not find " + base_dir)
        elif response.status_code == 200:
            j = json.loads(response.text)
            id_list = []
            if type(j) == type(id_list):

                for l in j:
                    id_list.append(l["id"])
                for i in id_list:
                    new_base_dir = base_dir + "/" + i
                    crawl(new_base_dir)


def get_aland_links(links_list):
    with open(links_list, "rb") as f:
        api_links = pickle.load(f)
    print(api_links)

crawl(base_dir)
print("Finished!")
for b in buffer:
    print(b + "\n")
print(len(buffer))
with open("api_links.pkl", "wb") as f:
    pickle.dump(buffer, f)

