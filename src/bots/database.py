#%%
from tinydb import TinyDB, Query, where
from tinydb.operations import delete
import os

db_folder = os.path.join(os.path.dirname(__file__))
db_file = os.path.join(db_folder, 'database.json')
db = TinyDB(db_file)

table = db.table('Initializedchannelsanddata')
table1 = db.table('Designdecisions')
ch = Query()
#%%

def get_channel_details(channel_id):
    query_result = table.search(ch.channel.channelid == channel_id)
    if len(query_result) != 0:
        result = query_result[0]['channel']
    else:
        result = None

    return result
#%%

def get_all_decisions(channel_id=None):
    if channel_id is None:
        result = []
        for _decision in table1.all():
            result.append(_decision['decisions'])
    else:
        query_result = table1.search(ch.decisions.channelid == channel_id)
        result = []
        for _decision in query_result:
            result.append(_decision['decisions'])

    return result
#%%


def get_all_entries(table_name):
    _table = db.table(table_name)
    result = _table.all()
    return result
#%%
def get_all_database():
    _tables = db.tables()
    result = {}
    for table_name in _tables:
        _table = db.table(table_name)
        result[table_name] = _table.all()

    return result
#%%

# def insert_decision(decision, channel_id):
#     pass

# def delete_decision(decision, channel_id):
#     pass

# def insert_channel(channel_id,channel_name,vphase,member,phase_date):
#     table.insert({'channel': {'channelid': channel_id, 'channelname' : channel_name ,'vphase' : vphase, 'membername' : member, 'phasedate' : phase_date}})
#     pass

# def delete_channel(channel_id):
#     table.remove(where('channel').channelid == channel_id)
#     pass

# def find_channel_exists(channel_id):
#     table.search(ch['channel']['channelid'] == channel_id)
#     pass


