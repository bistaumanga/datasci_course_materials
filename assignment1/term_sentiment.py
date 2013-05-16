import sys, json

def calcScore(wordScores, tweetText):
    '''calcultion of sentiment score for each tweet'''

    
    words = tweetText.encode('utf8').lower().split()
    score = 0

    for word in words :
        if word in wordScores:
            score +=wordScores[word]
    return score

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    #Read word-sentiment scores from file into dictionary
    lines = [line.split('\t') for line in sent_file.readlines()]
    wordScores = {word : int(score) for (word, score) in lines}
    
    # Reading tweet file
    tweets = [json.loads(tweet) for tweet in tweet_file.readlines()]
    additionalWords = {}

    for tweet in tweets:
        try:
            tweetText = tweet['text']
            score = float(calcScore(wordScores, tweetText))
              
            words = tweetText.split()

            for word in words:
    			if word in additionalWords:
    				additionalWords[word]['mood'] += score
    				additionalWords[word]['occurence'] += 1
    			else:
    				additionalWords[word] = {'mood' : score, 'occurence' : 1}

        except Exception, e:
            #print 'exception : ' + str(e)
            pass

    for word, count in additionalWords.items():
    	print word.encode('utf8'), float(count['mood']) / count['occurence']
    sent_file.close()
    tweet_file.close()

if __name__ == '__main__':
    main()