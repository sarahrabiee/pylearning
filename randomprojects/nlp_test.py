import tweepy
from textblob import TextBlob

consumer_key = 'BrbeTNAxu88V88doerPs1skxK'
consumer_secret = '2oJ0bve6PXYpVpVf4I231OyCXVZZKlc6uJQ7KWzBPBZphNIBfE'

access_token = '996854817946521600-tVGSAiRAU9w341JeNI9qt8bVxHfNEfv'
access_token_secret = 'xVkzuABODM7CxW1uIFcTkNb2utzng4pNcK26YE7QvvYO7'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
public_tweets = api.search('Trump')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)

