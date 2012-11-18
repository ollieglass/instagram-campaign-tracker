import requests
import json

from pymongo import Connection

CAMPAIGN = "uostyle"
INSTAGRAM_API_ACCESS_TOKEN = "XXXXXXXXXXXXXX"

# connect to mongo

connection = Connection()
db = connection['instagram']
collection = db[CAMPAIGN]


# download data from instagram

r = requests.get("https://api.instagram.com/v1/tags/%s/media/recent?access_token=%s" % (CAMPAIGN, INSTAGRAM_API_ACCESS_TOKEN))
collection.insert(r.json['data'])

next_max_tag_id = r.json['pagination']['next_max_tag_id']

while True:
	print "posts collected %s" % collection.count()
	print "next cursor %s" % next_max_tag_id

	r = requests.get("https://api.instagram.com/v1/tags/%s/media/recent?access_token=%s&max_id=%s" % (CAMPAIGN, INSTAGRAM_API_ACCESS_TOKEN, next_max_tag_id))
	collection.insert(r.json['data'])

	if 'next_max_tag_id' in r.json['pagination']:
		next_max_tag_id = r.json['pagination']['next_max_tag_id']
	else:
		print r.json

