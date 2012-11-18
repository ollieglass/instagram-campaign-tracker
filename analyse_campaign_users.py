import datetime
import json
from pprint import pprint
from collections import defaultdict
import operator

from pymongo import Connection
from jinja2 import Template

CAMPAIGN = "uostyle"
REPORT_TEMPLATE = 'top_fans_template.html'

# connect to mongo

connection = Connection()
db = connection['instagram']
collection = db[CAMPAIGN]

users_collection = db["%s_users" % CAMPAIGN]
users_collection.ensure_index("username")

# all users to the users_collection

for photo in collection.find():
	
	# likes 
	for person in photo['likes']['data']:
		users_collection.update({'username': person['username']}, person, upsert=True);

	# photo
	users_collection.update({'username': photo['user']['username']}, photo['user'], upsert=True);

	# comments
	for comment in photo['comments']['data']:
		users_collection.update({'username': comment['from']['username']}, comment['from'], upsert=True);

	# caption
	if photo['caption']:
		users_collection.update({'username': photo['caption']['from']['username']}, photo['caption']['from'], upsert=True);


# count all user engagement

for photo in collection.find():

	# likes 
	for person in photo['likes']['data']:
		users_collection.update({'username': person['username']}, 
			{'$inc': {'stats.likes':1, 'stats.total':1}})

	# photo
	users_collection.update({'username': photo['user']['username']}, 
		{'$inc': {'stats.photos':1, 'stats.total':1}})

	# comments
	for comment in photo['comments']['data']:
		users_collection.update({'username': comment['from']['username']}, 
			{'$inc': {'stats.comments':1, 'stats.total':1}})

	# caption
	if photo['caption']:
		users_collection.update({'username': photo['caption']['from']['username']}, 
			{'$inc': {'stats.captions':1, 'stats.total':1}})
