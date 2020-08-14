import time
def unique_list(list):
    unique_list = []
    for l in list:
        if l in unique_list:
            continue
        else:
            unique_list.append(l)
    return unique_list

def write_VALUES(parsed_data):
    key_list = list(parsed_data.keys())
    s = ""
    with open("new_px_file.txt", "wb") as f:
        for k in key_list[1:-1]:
            s = s + 'VALUES("{}")='.format(k)
            unique_v = unique_list(parsed_data[k])
            for v in unique_v:
                s = s + '"{}",'.format(v)
            s = s[:-1] + "; \n"
        print(s)

def write_meta_data():
    named_tuple = time.localtime() # get struct_time
    time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
    s = 'CHARSET="ANSI"; \nAXIS-VERSION="2010"; \nCODEPAGE="iso-8859-15"; \nLANGUAGE="sv"; \nLANGUAGES="sv","en";'
    s = s + '\nCREATION-DATE="{}";'.format(time_string)
    print(s)