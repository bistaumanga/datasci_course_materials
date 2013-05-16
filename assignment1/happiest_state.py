import sys, json, operator

def calcScore(wordScores, tweetText):
    '''calcultion of sentiment score for each tweet'''

    words = tweetText.encode('utf8').lower().split()
    score = 0
    for word in words :
        if word in wordScores:
            score +=wordScores[word]
    return float(score)

def computeHappiestState(wordScores, placeTweet):
	states = {}
	for state, text in placeTweet:
		if state in states:
			states[state] += calcScore(wordScores, text)
		else:
			states[state] = calcScore(wordScores, text)
	return max(states.iteritems(), key=operator.itemgetter(1))[0]

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    #Read word-sentiment scores from file into dictionary
    lines = [line.split('\t') for line in sent_file.readlines()]
    wordScores = {word : int(score) for (word, score) in lines}
    
    # Reading tweet file
    tweets = [json.loads(tweet) for tweet in tweet_file.readlines()]
    placeTweet = []
    for tweet in tweets:
    	if tweet.has_key('place'):
    		if tweet['place'] != None and tweet['place']['country_code'] == 'US':
    			placeTweet.append( (tweet['place']['full_name'].split(', ')[1],tweet['text']))
    #print placeTweet
    #statetweet = {'state' : tweet['place']['full_name'].split(',')[1], 'text' : tweet['text'] for tweet in tweets if tweet.has_key('place') and tweet['place'] != None and tweet['place']['full_name'] == 'US'}
    print computeHappiestState(wordScores,placeTweet)
    sent_file.close()
    tweet_file.close()

if __name__ == '__main__':
    main()