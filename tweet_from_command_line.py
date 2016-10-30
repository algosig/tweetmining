#Create a twitter account if you do not already have one.
#Go to https://apps.twitter.com/ and log in with your twitter credentials.
#Click "Create New App"
#Fill out the form, agree to the terms, and click "Create your Twitter application"
#In the next page, click on "API keys" tab, and copy your "API key" and "API secret".
#Scroll down and click "Create my access token", and copy your "Access token" and "Access token secret".
#Import the necessary methods from tweepy library

import tweepy
class TwitterAPI:
    def __init__(self):
        consumer_key = "zuGFRveD0kSTGdpNByZQUZgz7"
        consumer_secret = "uLGYKAJv2cfeUsJZR3jU71ERBjCbAzlWfcFZ9A1iWiaIXf8Oie"
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        access_token = "1158122640-jxtFTgCf5xBmrWpifz8Zc6G3okaQVKcTG6eLDMG"
        access_token_secret = "YVyW2wxTYDEiV3O300Fifs5WB8Dj7CvdfBfdg401lxsxU"
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def tweet(self, message):
        self.api.update_status(status=message)

if __name__ == "__main__":
    twitter = TwitterAPI()
    twitter.tweet("I Just tweeted from \#terminal .I'm \#learning \#tweepy & \#Python ")
