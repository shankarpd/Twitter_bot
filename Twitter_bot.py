from github import Github
from datetime import datetime
import tweepy
import time
from tweepy import OAuthHandler
import keys
# First create a Github instance:
d = datetime.today()
ckey = keys.ckey
csecret = keys.csecret
atoken = keys.atoken
asecret = keys.asecret
INTERVAL = 60 * 60 * 12

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)


# using username and password
g = Github(keys.username, keys.password)
days_updated= []
# Then play with your Github objects:
while True:
	for repo in g.get_user().get_repos():
		if d.date() == repo.updated_at.date():
			api.update_status(f'yes he did, he updated: {repo.name}')
	time.sleep(INTERVAL)
