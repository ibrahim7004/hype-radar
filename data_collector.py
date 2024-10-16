import tweepy
import yaml

with open('config/config.yaml', 'r') as config_file:
    config = yaml.safe_load(config_file)

auth = tweepy.OAuthHandler(
    config['twitter']['api_key'], config['twitter']['api_secret_key'])
auth.set_access_token(config['twitter']['access_token'],
                      config['twitter']['access_token_secret'])
api = tweepy.API(auth)


def collect_tweets(query, max_tweets):
    tweets = []
    for tweet in tweepy.Cursor(api.search_tweets, q=query, tweet_mode="extended", lang="en").items(max_tweets):
        tweets.append({
            'id': tweet.id,
            'text': tweet.full_text,
            'created_at': tweet.created_at,
            'user': tweet.user.screen_name,
            'likes': tweet.favorite_count,
            'retweets': tweet.retweet_count,
            'hashtags': [h['text'] for h in tweet.entities['hashtags']]
        })
    return tweets
