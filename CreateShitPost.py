"""
This is my second Twitter bot project.

I whant to create shitpost with multiple tweets.
"""

import tweepy
import time

#connection to the account
auth = tweepy.OAuthHandler("XMIEkLdfAiJcRAtCDUy7Y268u", "TNKhMNjgfVqHnLJ4PsoJXC5Lrsz9pjcUjABSNj5nHsliXaFZBW")
#connection to the app in Twitter developpement
auth.set_access_token("1588133381665071106-EdRy2HtcUn55wn41G54Vk4XOkmSyCD", "Tn6WoIV6heirjNISdUOKlMu6dgYCSOVKwGJu9YbqR7osa")

api = tweepy.API(auth)


try:
    api.verify_credentials()
    print("The bot is connected")

except:
    print("Connection error...")

while True:
    isTheTweetGood = False

    while(isTheTweetGood == False):
        print("starting a new tweet")
        word = "je"
        wordNumber = 0
        textTweet = word
        isAnyTweetLeft = True
        oldTweetId = ""

        while(isAnyTweetLeft):
            print("Collecting tweet...")

            try:
                tweets = api.search_tweets(q= word, lang= 'fr', count= 100)
                print("searching word " + word)

            except:
                print("search error, stop collecting tweets.")
                break

            isAnyTweetLeft = False;

            for tweet in tweets:
                text = str(tweet.text).split(' ')

                if len(text) > wordNumber and text[wordNumber] == word:
                    try:
                        if oldTweetId == tweet.id:
                            raise Exeption("tweet already quoted.")
                        else:
                            wordNumber += 1
                            word = text[wordNumber]
                            print("Tweet found, new word: " + word)
                            textTweet = textTweet + ' ' + word
                            isAnyTweetLeft = True
                            break
                    except:
                        print("tweet invalide.")
        if wordNumber >= 5:
            isTheTweetGood = True


    print(textTweet)
    api.update_status(textTweet)
    time.sleep(60)
