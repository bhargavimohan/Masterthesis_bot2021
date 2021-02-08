from tinydb import TinyDB, Query

DB = TinyDB('dbtest.json')
table = DB.table('user')
table.insert({'id': 1, 'username': 'Jhon'})

print(table.all())

