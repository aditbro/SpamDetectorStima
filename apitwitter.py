import tweepy

consumer_key = "JEutn3TayHnUiE1SRpBgGD5cS"
consumer_secret = "GYlh5oHNqWCAVQpUDEoTZqpI5FEdfh1SWu4paPHLbc9WFHlHaD"
access_token =  "343114738-tN14v5mju9CQ5hIP9cIZpHhnb1fSsgwWoIYUaRt9"
access_token_secret = "7MYgSEf0ZGQIo9ww3SRFKGUsYCKDZRhcMj9S4Fk2v5vC8"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

ftweet = open("tweets.txt","w")

public_tweets = api.search(q="*",count=500, lang="id")
for tweet in public_tweets:
	ftweet.write("{{\n")
	ftweet.write(str(tweet.text.encode('utf-8')))
	ftweet.write("\n}}\n")
ftweet.close()