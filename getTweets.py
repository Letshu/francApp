from sqlalchemy import null
import tweepy

BREARER_TOKEN="AAAAAAAAAAAAAAAAAAAAAOxyigEAAAAAOGHUM1EXH7mWoDJvodWEnbAnCis%3DVr8NspYA5kn4GjWj19xOcSDPFj1KcDzFdGW5Lqerq1QeJeQQjW"



def getUserTweets(userName):
    client = tweepy.Client(bearer_token=BREARER_TOKEN, wait_on_rate_limit=False)
    user = client.get_user(username= userName)
    userId=user.data.id
    user = client.get_user(id=userId)
    tweets = client.get_users_tweets(id=userId, tweet_fields=['id', 'text', 'created_at', 'context_annotations'])
    return tweets.data
    
#getUserTweets("WilliamLetchu")

def getUserFollower(userName):
    client = tweepy.Client(bearer_token=BREARER_TOKEN, wait_on_rate_limit=True)
    user = client.get_user(username= userName)
    userId=user.data.id
    followers = client.get_users_followers(id=userId)
    followers_tweets = {}
    for i,follower in enumerate(followers.data):
        tweets_posted = getFollowerTweets(str(follower))
        if tweets_posted is not None:
            followers_tweets[str(follower)]= tweets_posted
        else:
            followers_tweets[str(follower)]= ["No tweets"]
    
    return followers_tweets
        
        
def getFollowerTweets(userName):
    client = tweepy.Client(bearer_token=BREARER_TOKEN, wait_on_rate_limit=True)
    try:
        user=client.get_user(username=userName).data
    except:
        return null
    user_id = user.id
    tweets = client.get_users_tweets(id=user_id, tweet_fields=['id', 'text', 'created_at', 'context_annotations'])
    return tweets.data

    


# print("+++++++++++++++++++++++++++++++++++++++")
# print("My own tweets")
# getUserTweets("WilliamLetchu")
# print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
# print("My follower's tweets")
# getUserFollower("WilliamLetchu")
