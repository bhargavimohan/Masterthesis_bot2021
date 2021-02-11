from tinydb import TinyDB, Query,where
from tinydb.operations import delete
db = TinyDB('db.json')


table = db.table('Initializedtables')
def create_tables(cn, vn):
    table.insert({cn: vn})  
    print(table.all())
    ch = Query()
    result = table.search(ch[cn] == vn)
    if len(result) >= 1:
        table.remove(where(cn) == vn)

    

    # for table_name in db.tables():
    #     print(table_name)
    #     table = db.table(table_name)
    #     print(table.all())

# db.drop_tables()
# db.truncate()
create_tables('channel_1','MB')





