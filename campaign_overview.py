import datetime
import json
from pprint import pprint

from pymongo import Connection

CAMPAIGN = "uostyle"

# connect to mongo

connection = Connection()
db = connection['instagram']
collection = db[CAMPAIGN]


# stats we're interested in

start_date = None
end_date = None
likes = 0
users = []
likers = {}
captions = []


for photo in collection.find():
	# date
	photo_date = int(photo['created_time'])
	
	if start_date is None:
		start_date = photo_date
	if end_date is None:
		end_date = photo_date

	if photo_date < start_date:
		start_date = photo_date

	if photo_date > end_date:
		end_date = photo_date

	# likes + likers
	likes += photo['likes']['count']

	for person in photo['likes']['data']:
		likers[person['username']] = person

	# user
	users.append(photo['user'])

	# caption
	if photo['caption']:
		captions.append(photo['caption']['text'])

start_date = datetime.datetime.fromtimestamp(start_date)
end_date = datetime.datetime.fromtimestamp(end_date)

print "Instagram activity between %s and %s" % (
	start_date.strftime('%Y-%m-%d %H:%M:%S'),
	end_date.strftime('%Y-%m-%d %H:%M:%S')
)

campaign_duration = end_date - start_date
print "Campaign duration: %s" % str(campaign_duration)
print "Photos shared: %s" % collection.count()
print "Users: %s" % len(users)
print "Likers: %s" % len(likers)
print "Likes: %s" % likes

# print users
# pprint(likers)
# pprint(captions)