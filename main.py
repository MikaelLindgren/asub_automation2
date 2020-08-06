import mysql
import json
import requests as r
import extract
from database import cursor
import database_dude
import querymaker
api_dir = "http://pxnet2.stat.fi/PXWeb/api/v1/sv/StatFin/kan/altp/statfin_altp_pxt_12bc.px"
#api_dir = "http://pxnet2.stat.fi/PXWeb/api/v1/sv/StatFin/ene/asen/statfin_asen_pxt_11zr.px"
generated_json = querymaker.make_query(api_dir)
with open(generated_json) as f:
    js = json.loads(f.read())
    print(js)
    response = r.post(api_dir, json = js)
    print(response.text)
    tree = json.loads(response.text)
    col = extract.orienter(tree) #list
    ticks = extract.get_axis_ticks(tree) #dictionary
    size = extract.get_size(tree) #touple
    labels = extract.get_axis_labels(tree) #dictionary
    values = extract.get_values(tree) #list
    #print(col)
    #print(ticks)
    #print(size)
    #print(labels)
    #print(values)
    lab = []
    for k in labels.keys():
        lab.append(labels[k])
    title = extract.title_getter(api_dir)
    database_dude.add_table(lab,title,"acme")
    print(size)
    print("done!")
    #entries = database_dude.fill_table(title, col, ticks, size, lab, values)
    #database_dude.actually_add(entries, "acme")
    print(size)

