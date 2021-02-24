#%%
from tinydb import TinyDB, Query, where
from tinydb.operations import delete
import os

db_folder = os.path.join(os.path.dirname(__file__))
db_file = os.path.join(db_folder, 'database.json')
db = TinyDB(db_file)

channelstable = db.table('Initializedchannelsanddata')
decisionstable = db.table('Designdecisions')
ch = Query()
#%%

def get_channel_details(channel_id):
    query_result = channelstable.search(ch.channel.channelid == channel_id)
    if len(query_result) != 0:
        result = query_result[0]['channel']
    else:
        result = None

    return result
#%%

def get_all_decisions(channel_id=None):
    if channel_id is None:
        result = []
        for _decision in decisionstable.all():
            result.append(_decision['decisions'])
    else:
        query_result = decisionstable.search(ch.decisions.channelid == channel_id)
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

def insert_decision(channel_id,channel_name,memberid,decisiondate,a,user_text1,b,user_text2,c,user_text3):
    decisionstable.insert({'decisions': {'channelid': channel_id, 'name' : channel_name , 'membername' : memberid, 
            'date' : decisiondate,'decisionname_a': a,'decision_a': user_text1[0],'decisionname_b': b,'decision_b': user_text2[0],
            'decisionname_c': c,'decision_c': user_text3[0]}})
    return True

def delete_decision(channel_id):
    decisionstable.remove(where('decisions').channelid == channel_id)
    return True

def insert_channel(channel_id,channel_name,vphase,member,cardsentdate):
    channelstable.insert({'channel': {'channelid': channel_id, 'name' : channel_name ,'vphase' : vphase, 'membername' : member, 'date' : cardsentdate}})
    return True

def delete_channel(channel_id):
    channelstable.remove(where('channel').channelid == channel_id)
    return True

def find_channel_exists(channel_id):
    result = channelstable.search(ch['channel']['channelid'] == channel_id)
    return result



# %%
