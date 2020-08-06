import requests as r 
import json
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

# def alandify(list_of_areas):
#     intersting = {}
#     interestin_inv = {}
#     intersting_values = ["Hela landet", "Fasta Finland", "Nyland", "Egentliga Finland", "Birkaland", "Österbotten", "Åland", "Åland", "Åland", "Helsingfors-Nyland", "Brändö", "Eckerö", "Finström", "Föglö", "Geta", "Hammarland", "Jomala", "Kumlinge", "Kökar", "Lemland", "Lumparland", "Saltvik", "Sottunga", "Sund", "Vårdö", "Mariehamn"]
#     interesting_keys = ["SSS", "MA1", "MK01", "MK02", "MK06", "MK15", "MK21", "SA5", "MA2", "SA1", "035", "043", "060", "062", "065", "076", "170", "295", "318", "417", "438", "736", "766", "771", "941", "478"
#     iv = 0
#     for ik in interesting_keys:
#         interesting[ik] = intersting_values[iv]
#         interesting_inv[intersting_values[iv]] = ik
#         iv = iv + 1
    
#     idoa = {}
#     idoa_inv = {}
#     for a in list_of_areas:
#         if a in interesting_keys:
#             idoa[a] = interesting[a]
#             idoa_inv[interesting[a]] = a
#     return idoa, idoa_inv
