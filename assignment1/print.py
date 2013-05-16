import urllib
import json

response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft")
pyresponse = json.load(response)
results = pyresponse["results"]
#print results[7]["text"]
for i in range(10):
	tweet = results[i]["text"]
	print tweet.encode('utf-8')