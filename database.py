import mysql.connector as mc

config = {
    'user' : 'root',
    'password' : 'Hebedewski913',
    'host' : 'localhost'
}
db = mc.connect(**config)
cursor = db.cursor()
