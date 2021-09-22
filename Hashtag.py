import requests
import json


def hashtag(text):
	result = requests.get("http://127.0.0.1:5000/hashtag/" +text) 
	return json.loads(result.text)['hashtaged']
