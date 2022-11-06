"""
This is my second Twitter bot project.

I whant to post every minuts one tweet whitch cotain the word "merde"
"""

import tweepy
import time

#connection to the account
auth = tweepy.OAuthHandler("XMIEkLdfAiJcRAtCDUy7Y268u", "TNKhMNjgfVqHnLJ4PsoJXC5Lrsz9pjcUjABSNj5nHsliXaFZBW")
#connection to the app in Twitter developpement
auth.set_access_token("1588133381665071106-EdRy2HtcUn55wn41G54Vk4XOkmSyCD", "Tn6WoIV6heirjNISdUOKlMu6dgYCSOVKwGJu9YbqR7osa")

api = tweepy.API(auth)

#counter of tweets
i = 1

try:
    api.verify_credentials()
    print("The bot is connected")

except:
    print("Connection error...")

while True:
    tweets = api.search_30_day(label = "dev",query =  "merde", maxResults = 100)


    for tweet in tweets:

        print(tweet.user.screen_name)

        try:
            api.update_status("J'ai trouvé ceci pour la gloire de mon créateur:", attachment_url = "https://twitter.com/" + tweet.user.screen_name + "/status/" + tweet.id_str)
            print(str(i) + ": " + tweet.text + "\n")
            i += 1
            time.sleep(60)
        except:
            print("already retweeted.")
