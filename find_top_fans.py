import datetime
import json
from pprint import pprint
from collections import defaultdict
import operator

from pymongo import Connection

CAMPAIGN = "uostyle"

# connect to mongo

connection = Connection()
db = connection['instagram']
collection = db[CAMPAIGN]


# stats we're interested in

users = defaultdict(int)

for photo in collection.find():
	
	# likes 
	for person in photo['likes']['data']:
		users[person['username']] += 1

	# photo
	users[photo['user']['username']] += 1

	# comments
	for comment in photo['comments']['data']:
		users[comment['from']['username']] +=1

	# caption
	if photo['caption']:
		users[photo['caption']['from']['username']] +=1


users = sorted(users.iteritems(), key=operator.itemgetter(1), reverse=True)

pprint(users[:20])

print "Total users %s" % len(users)