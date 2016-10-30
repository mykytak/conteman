from utils import *
import shelve

WORKING_DIR = '/home/xedar/devel/workflowScripts/python'
DB_FILE = '/home/xedar/devel/workflowScripts/python/db.shelve'

states = {
    'work': {
        'can':   ['work', 'urgent'],
        'delay': ['time']
    },
    'rest': {
        'can':   ['any'],
        'delay': []
    }
}

events = {
    'work': [
        { 'type': 'work'
        , 'time': '* /1 * * 1-3'
        }
    ]
}

query = {
    '* * * * *'
}

db = shelve.open(DB_FILE)
db['state']
db['events']


# actions = {
#         'set': 
#         'clear':
#         'list':
#     }

# test()

# test = State('test', 'something')

# print("%s => %s" % (test.name, test.allowed))


# get action
# run bash script or do action
# if fron cron - check is work in progress (then shows nothing). If not - send message.
# 

