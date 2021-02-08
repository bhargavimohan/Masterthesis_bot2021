from tinydb import TinyDB, Query
db = TinyDB('db.json')


def create_tables(channel_vmodel,sender_name,date,desicion_message):
    table = db.table(channel_vmodel)
    table.insert({'sender_name': sender_name})
    table.insert({'date': date})
    table.insert({'desicion_message': desicion_message})   
    for table_name in db.tables():
        print(table_name)
        table = db.table(table_name)
        print(table.all())

# db.drop_tables()
# db.truncate()
create_tables('teamD_Model based','member1','2020-02-08','MB decision')





