import json
import requests as r
import extract
from database import cursor, db


def make_query(api_dir):
    response = r.get(api_dir)
    rt = response.text
    jl = json.loads(rt)
    cv = {}
    for k in jl.keys():
        pass
    for l in jl["variables"]:
        c = l["code"]
        v = l["values"]
        cv[c] = v
    with open("gen_query.json", "w") as f:
        s = '{"query": ['
        for c in cv:
            s = s + '{ "code" : "'+ c +  '", "selection": {"filter": "item", "values": ['
            for v in cv[c]:
                s = s+'"{}",'.format(v)
            s = s[:-1]
            s = s + "] } } ,"
        s = s[:-1] + '], "response": { "format": "json-stat" } }'
        js = json.loads(s)
        jsd = json.dumps(js, indent = 4)
        f.write(jsd)
    return "gen_query.json"



def alandify(list_of_areas):
    intersting = {}
    interestin_inv = {}
    intersting_values = ["Hela landet", "Fasta Finland", "Nyland", "Egentliga Finland", "Birkaland", "Österbotten", "Åland", "Åland", "Åland", "Helsingfors-Nyland" ]
    interesting_keys = ["SSS", "MA1", "MK01", "MK02", "MK06", "MK15", "MK21", "SA5", "MA2", "SA1" ]
    kommuner_n = ["035", "043", "060", "062", "065", "076", "170", "295", "318", "417", "438", "736", "766", "771", "941", "478"]
    kommuner = ["Brändö", "Eckerö", "Finström", "Föglö", "Geta", "Hammarland", "Jomala", "Kumlinge", "Kökar", "Lemland", "Lumparland", "Saltvik", "Sottunga", "Sund", "Vårdö", "Mariehamn"]


def contains_kommun(area):
    for k in kommuner_n:
        if area.endswith(k):
            return True
    return False
