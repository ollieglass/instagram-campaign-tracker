# -*- coding: utf8 -*- 

import datetime
import json
from pprint import pprint
from collections import defaultdict
import operator

import pymongo
from jinja2 import Template

CAMPAIGN = "uostyle"
REPORT_TEMPLATE = 'top_fans_template.html'
NUM_TOP_USERS = 20

# connect to mongo

connection = pymongo.Connection()
db = connection['instagram']
collection = db[CAMPAIGN]

users_collection = db["%s_users" % CAMPAIGN]
users_collection.ensure_index("username")

# get top users
top_users = list(users_collection.find().sort('stats.total',pymongo.DESCENDING).limit(NUM_TOP_USERS))
total_users = users_collection.count()

# build report

template = Template(open(REPORT_TEMPLATE, 'r').read())
report = template.render(
	campaign=CAMPAIGN,
	total_users=total_users,
	top_users=top_users
)

report = unicode(report).encode('utf8')
print report

