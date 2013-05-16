import json, sys

def main():
    tweets = [json.loads(tweet) for tweet in open(sys.argv[1]).readlines()]
    countList = {}
    for tweet in tweets:
        try:
            tweetText = tweet['text']
            words = tweetText.split()
            for word in words:
                if word in countList:
                    countList[word] += 1
                else:
                    countList[word] = 1
        except Exception, e:
            #print 'exception :' + str(e)
            pass

    total = sum(count for word, count in countList.items())
    #x = 0.0
    for word, count in countList.items():
        #x += float(count) / total
        print word.encode('utf8'), float(count) / total
    #print x

if __name__ == '__main__':
    main()
