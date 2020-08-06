import mysql
import json
import requests as r 

def get_axis_ticks(tree):
    col = orienter(tree)
    tree = tree["dataset"]
    all_lists = {}
    for c in col:
        klist = []
        branch = tree["dimension"][c]["category"]["label"]
        for k in branch.keys():
            klist.append(branch[k])
        all_lists[c] = klist
    return all_lists

def get_size(tree):
    return tree["dataset"]["dimension"]["size"]

def get_axis_labels(tree):
    col = orienter(tree)
    tree = tree["dataset"]
    labels = {}
    for c in col:
        labels[c] = tree["dimension"][c]["label"]
    return labels        
def orienter(tree):
    tree = tree["dataset"]
    col = tree["dimension"]["id"]
    return col
def get_values(tree):
    tree = tree["dataset"]
    values = tree["value"]
    return values
def title_getter(api_dir):
    t = r.get(api_dir)
    title = json.loads(t.text)["title"]
    title_parts = title.split(",")
    return title_parts[0].replace(" ","")
