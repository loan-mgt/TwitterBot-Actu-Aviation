import tweepy
import requests
import Key

# Authenticate to Twitter
#auth = tweepy.OAuthHandler("KEY", "SECRET_KEY")
#auth.set_access_token("TOKEN", "SECRET_TOKEN")
auth = tweepy.OAuthHandler(Key.tweet_key, Key.tweet_secrete)
auth.set_access_token(Key.tweet_token, Key.tweet_token_secrete)

# Create API object
api = tweepy.API(auth)

def tweet(img,msg):
	
	r = requests.get(img, allow_redirects=True)

	open('tmp.png', 'wb').write(r.content)
	api.update_with_media(filename='tmp.png',status=msg)
