from tinydb import TinyDB, Query,where
from tinydb.operations import delete
db = TinyDB('db.json')

table = db.table('Initializedtables')
table.insert({"test": "value"})
ch = Query()
table.search(ch["test"] == "value")
print(table.all())