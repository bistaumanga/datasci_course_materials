import sys, json, operator, itertools

def main():
    tweet_file = open(sys.argv[1])

    # Reading tweet file
    tags={}
    tweets = [json.loads(tweet) for tweet in tweet_file.readlines()]
    for tweet in tweets:
        if tweet.has_key('entities'):
            if tweet['entities']['hashtags'] != []:
                for x in tweet["entities"]["hashtags"]:
                    if x['text'] in tags:
                        tags[x['text'].encode('utf-8')] += 1
                    else:
                        tags[x['text'].encode('utf-8')] = 1

    s = sorted(tags.iteritems(), key=operator.itemgetter(1))[-10:] #last 10
    for key, value in s[::-1]: #reversing
        print key, float(value)
    tweet_file.close()

if __name__ == '__main__':
    main()