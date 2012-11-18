import datetime
import json
from pprint import pprint

data = json.load(open('urban_outfitters_instagram_campaign.json'))

# stats we're interested in
start_date = None
end_date = None
likes = 0
users = []
likers = {}
captions = []

for item in data:
	# date
	photo_date = int(item['created_time'])
	
	if start_date is None:
		start_date = photo_date
	if end_date is None:
		end_date = photo_date

	if photo_date < start_date:
		start_date = photo_date

	if photo_date > end_date:
		end_date = photo_date

	# likes + likers
	likes += item['likes']['count']

	for person in item['likes']['data']:
		likers[person['username']] = person

	# user
	users.append(item['user'])

	# caption
	if item['caption']:
		captions.append(item['caption']['text'])

start_date = datetime.datetime.fromtimestamp(start_date)
end_date = datetime.datetime.fromtimestamp(end_date)

print "Instagram activity between %s and %s" % (
	start_date.strftime('%Y-%m-%d %H:%M:%S'),
	end_date.strftime('%Y-%m-%d %H:%M:%S')
)

campaign_duration = end_date - start_date
print "Campaign duration: %s" % str(campaign_duration)
print "Photos shared: %s" % len(data)
print "Users: %s" % len(users)
print "Likers: %s" % len(likers)
print "Likes: %s" % likes

# print users
# pprint(likers)
# pprint(captions)