import mysql.connector as mc
from mysql.connector import errorcode
import json
import requests as r
import extract
from database import cursor, db

def add_table(labels, table_name, DB_NAME):
    TABLE = (
        "CREATE TABLE `{}` ("
        "`id` int(11) AUTO_INCREMENT,".format(table_name)
    )
    for l in labels:
        TABLE = TABLE + (
        " `{}` varchar(255) NOT NULL,".format(l)
        )
    TABLE = TABLE + (
        " `{}` varchar(255),".format("Värden")
    )
    TABLE = TABLE + (
        "PRIMARY KEY (`id`)"
        ") ENGINE=InnoDB"
    )
    cursor.execute("USE {}".format(DB_NAME))
    try:
        print("Creating table ({}) in database {}...".format(table_name,DB_NAME))
        cursor.execute(TABLE)
    except mc.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("Table ({}) already exists.".format(table_name))
        else:
            print(err.msg)
    
def get_entry_instruction(table_name, label_names, coordinates, value):
    sql = "INSERT INTO " + table_name + " ("
    for ln in label_names:
        sql = sql + ln.replace(",","") + ", "
    sql = sql + "Värden"
    sql = sql + ") VALUES ("
    for c in coordinates:
        sql = sql +"'{}'".format(c.replace(",","").replace(" ", "")) + ", "
    sql = sql + "'{}'".format(str(value))
    sql = sql + ")"
    return sql
    cursor.execute(sql)
    db.commit()

def fill_table(table_name, col, ticks, size, labels, values):
    entries = []
    values_names = []
    buffer = []
    get_pairs(ticks, col, [], buffer)
    i = 0
    for b in buffer:
        entry = get_entry_instruction(table_name, labels, b, values[i])
        entries.append(entry)
        i = i+1
    return(entries)
def get_pairs(ticks, col, so_far, buffer):
    if len(col) > 0:
        for t in ticks[col[0]]:

            get_pairs(ticks, col[1:],so_far + [t], buffer)
    else:
        buffer.append(so_far)
def actually_add(entries, DB_NAME):
    for e in entries:
        print(e)
        cursor.execute("USE {}".format(DB_NAME))
        cursor.execute(e)
        db.commit()
    print("Finished adding!")




