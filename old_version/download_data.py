import requests
import json

# download data from instagram
hashtag = "uostyle"
access_token = "XXXXXXXXXXXXXX"

data = []

r = requests.get("https://api.instagram.com/v1/tags/%s/media/recent?access_token=%s" % (hashtag, access_token))
data.extend(r.json['data'])
next_max_tag_id = r.json['pagination']['next_max_tag_id']

while True:
	print next_max_tag_id
	r = requests.get("https://api.instagram.com/v1/tags/%s/media/recent?access_token=%s&max_id=%s" % (hashtag, access_token, next_max_tag_id))
	data.extend(r.json['data'])
	next_max_tag_id = r.json['pagination']['next_max_tag_id']

	data_file = open('urban_outfitters_instagram_campaign.json', 'w')
	data_file.write(json.dumps(data))
	data_file.close()
