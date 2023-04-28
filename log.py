import tweepy
import appInfo

def setApi():
    #connection to the account
    auth = tweepy.OAuthHandler(appInfo.getApi("key"), appInfo.getApi("secret"))
    #connection to the app in Twitter developpement
    auth.set_access_token(appInfo.getToken("key"), appInfo.getToken("secret"))

    api = tweepy.API(auth, wait_on_rate_limit= True)

    #verify connection
    try:
        api.verify_credentials()
        print("The bot is connected")

    except:
        print("Connection error...")
        exit()

    return api


