#!/usr/bin/env python
"""
    Collect Tweets from Twitter
"""
import tweepy
import json
from kafka import KafkaProducer
from kafka.errors import KafkaError

KAFKA_HOST = 'localhost:9092'
TOPIC = 'twitter'

def load_credentials(filename):
    """
    Load AWS and Twitter Credentials
    """
    with open(filename) as handle:
        credentials = json.load(handle)
        _twitter_creds = credentials["twitter"]

        return _twitter_creds

#loading credentials
twitter_creds = load_credentials("key.json")

#Twitter auth
twitter_auth = tweepy.OAuthHandler(twitter_creds['CONSUMER_KEY'], twitter_creds['CONSUMER_SECRET'])
twitter_auth.set_access_token(twitter_creds['ACCESS_TOKEN'], twitter_creds['ACCESS_TOKEN_SECRET'])

#Twitter API object
twitter_api = tweepy.API(twitter_auth, wait_on_rate_limit_notify=True, retry_count=3, retry_delay=5)

class StreamListener(tweepy.StreamListener):
    """
        Stream Listener
    """

    producer = KafkaProducer(bootstrap_servers=[KAFKA_HOST])
    def on_data(self, data):
        """
            On proper status
        """
        try:
            json_data = json.loads(data)
            if (json_data is not None and
                    json_data['text'] is not None):

                # Convert unicode to string
                tweet = str(json_data['text'])
                print tweet
                future = self.producer.send(TOPIC, tweet)


        except (KeyError, UnicodeDecodeError, Exception) as e:
            pass

    def on_error(self, status_code):
        """
            handle error of listener
        """
        if status_code == 420:
            print "YOU ARE BEING RATE LIMITED"
            return True  #Do not disconnect stream

def main():
    """
        main method of script
    """
    print "Streaming Tweets and sending to Kafka..."

    stream_listener = StreamListener()
    while True:
        try:
            streamer = tweepy.Stream(twitter_api.auth,
                listener=stream_listener)
            streamer.filter(locations=[-180, -90, 180, 90], languages=['en'])
        except Exception as e:
            print "Ignore: Malformed tweet or tweepy bug"

if __name__ == '__main__':
    main()
