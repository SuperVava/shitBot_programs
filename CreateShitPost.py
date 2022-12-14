"""
This is my second Twitter bot project.

I whant to create shitpost with multiple tweets.
"""

import tweepy
import time
import log

#connection to the account
auth = tweepy.OAuthHandler(log.getApi("key"), log.getApi("secret"))
#connection to the app in Twitter developpement
auth.set_access_token(log.getToken("key"), log.getToken("secret"))

api = tweepy.API(auth)

#verify connection
try:
    api.verify_credentials()
    print("The bot is connected")

except:
    print("Connection error...")
    exit()

#main loop
while True:

    #to check if the tweet is long enough
    isTheTweetGood = False

    while(isTheTweetGood == False):
        #variable set
        print("starting a new tweet")
        word = "je"
        wordNumber = 0
        textTweet = word
        isAnyTweetLeft = True
        oldTweetId = ""
        #while the robot found tweets
        while(isAnyTweetLeft):
            #print("Collecting tweet...")
            #set value to false if the program don't find anny tweet good for use
            isAnyTweetLeft = False;
            #searching tweets with the previous word in the message (begginin with 'je')
            try:
                tweets = api.search_tweets(q= word, lang= 'fr', count= 100, tweet_mode= 'extended')
                print("searching word " + word)
            except Exception as e:
                print(e)
                print("search error, stop collecting tweets.")
                break
            #for every result
            for tweet in tweets:
                #split each word
                text = str(tweet.full_text).split(' ')
                #if the tweet is long enough and contain the wrd in the right place
                try:
                    #don't use the same tweet twice
                    if oldTweetId == tweet.id:
                        raise Exception("tweet already quoted.")
                    #update values of variables
                    elif text.index(word) + 1 > len(text):
                        raise Exception("tweet too short")
                    else:
                        wordNumber += 1
                        word = text[text.index(word) + 1]
                        oldTweetId = tweet.id
                        print("Tweet found: " + tweet.user.screen_name + ": " + tweet.full_text)
                        print("New word: " + word)
                        textTweet = textTweet + ' ' + word
                        isAnyTweetLeft = True
                        break
                except Exception as e:
                    print(e)
        #if there is no tweet left, end loop
        if wordNumber >= 5: isTheTweetGood = True

    #add the hashtags
    textTweet = textTweet + '\n#shitpost #d??chet #??boueur #profitonsAvantLeGenocide #epargesNousElon'
    #tweet the shitpost and wait
    print(textTweet)
    api.update_status(textTweet)
    time.sleep(120)
