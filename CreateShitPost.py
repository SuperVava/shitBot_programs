"""
This is my second Twitter bot project.

I whant to create shitpost with multiple tweets.
"""

import time
import log
import autoReply
from colorama import Fore, init
init()

api = log.setApi()
listOfTweets = []

#main loop
while True:

    #to check if the tweet is long enough
    isTheTweetGood = False

    while(isTheTweetGood == False):
        #variable set
        print(Fore.YELLOW + "starting a new tweet" + Fore.WHITE)
        word = "je"
        wordNumber = 0
        textTweet = word
        isAnyTweetLeft = True
        oldTweetId = ""
        listOfTweets = []
        #while the robot found tweets
        while(isAnyTweetLeft):
            #print("Collecting tweet...")
            #set value to false if the program don't find anny tweet good for use
            isAnyTweetLeft = False
            #searching tweets with the previous word in the message (begginin with 'je')
            try:
                tweets = api.search_tweets(q= word, lang= 'fr', count= 100, tweet_mode= 'extended')
                print(Fore.YELLOW + "searching word " + word + Fore.WHITE)
            except Exception as e:
                print(e)
                print(Fore.RED + "search error, stop collecting tweets."+ Fore.WHITE)
                break
            #for every result
            for tweet in tweets:
                #split each word
                text = str(tweet.full_text).split(' ')
                #if the tweet is long enough and contain the wrd in the right place
                try:
                    #don't use the same tweet twice
                    if oldTweetId == tweet.id:
                        raise Exception(Fore.RED + "tweet already quoted."+ Fore.WHITE)
                    #update values of variables
                    elif text.index(word) + 1 > len(text):
                        raise Exception(Fore.RED + "tweet too short"+ Fore.WHITE)
                    else:
                        wordNumber += 1
                        word = text[text.index(word) + 1]
                        oldTweetId = tweet.id
                        print("Tweet found: " + tweet.user.screen_name + ": " + tweet.full_text)
                        print(Fore.GREEN + "New word: " + word + Fore.WHITE)
                        textTweet = textTweet + ' ' + word
                        listOfTweets.append(oldTweetId)
                        isAnyTweetLeft = True
                        break
                except Exception as e:
                    print(Fore.RED)
                    print(e)
                    print(Fore.WHITE)
        #if there is no tweet left, end loop
        if (wordNumber >= 5) & (len(textTweet) < 250): isTheTweetGood = True

    #add the hashtags
    textTweet = textTweet + '\n#shitpost #déchet #éboueur'
    #tweet the shitpost and wait
    print(textTweet)
    api.update_status(textTweet)
    userAlreadyNotified = []
    for id in listOfTweets:
        text = str(textTweet).split(' ')
        word = text[listOfTweets.index(id)]
        if((id not in userAlreadyNotified) & ('/' not in word)):
            try:
                print("ans. to " + "@" + api.get_status(id).user.screen_name + "for the word: " + word)
                api.update_status(status = "@" + api.get_status(id).user.screen_name + " Bonjour, le mot ou l'expression \"" + word + "\" a été utilisé pour composé un shitpost. Merci de votre contribution à la décheterie spirituelle.", in_reply_to_status_id = id) 
                userAlreadyNotified.append(id)
                print(Fore.GREEN + "Done"+ Fore.WHITE)
            except Exception as e:
                print(Fore.RED)
                print(e)
                print(Fore.WHITE)
        else: 
            print(Fore.RED + "Already notified or word is a link."+ Fore.WHITE)
        time.sleep(2)   
    autoReply.update()
    time.sleep(300)

    