import mysql
import json
import requests as r
import extract
from database import cursor
import database_dude
import querymaker
api_dir = "http://pxnet2.stat.fi/PXWeb/api/v1/sv/StatFin/kan/altp/statfin_altp_pxt_12bc.px"
#api_dir = "http://pxnet2.stat.fi/PXWeb/api/v1/sv/StatFin/ene/asen/statfin_asen_pxt_11zr.px"
api_dir = "http://pxnet2.stat.fi/PXWeb/api/v1/sv/StatFin/kan"

response = r.get(api_dir)
j = json.loads(response.text)
print(j)
print(type(j))
# print(j["variables"])
# for l in j["variables"]:
#     print(l.keys())

# generated_json = querymaker2.make_query(api_dir)
# with open(generated_json) as f:
#     js = json.loads(f.read())
#     print(js)
#     response = r.post(api_dir, json = js)
#     print(response.text)
#     tree = json.loads(response.text)
#     col = extract2.orienter(tree) #list
#     ticks = extract2.get_axis_ticks(tree) #dictionary
#     size = extract2.get_size(tree) #touple
#     labels = extract2.get_axis_labels(tree) #dictionary
#     values = extract2.get_values(tree) #list