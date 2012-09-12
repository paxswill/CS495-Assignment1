#!/usr/bin/env python

import twitter

def post(api_handle, tweet):
    api_handle.PostUpdate(tweet)

def last_100(api_handle, username):
    tweets = api_handle.GetUserTimeline(username, count=100)
    return tweets

def list_hashtags(tweets):
    hashtags = set()
    for tweet in tweets:
        hashtags.update(filter(
            (lambda s: s[0] == u'#'),
            filter((lambda s: len(s) > 2), tweet.text.split(' '))))
    return hashtags


def main():
    # Read in the secrets
    secrets = dict()
    for key in ('consumer_key',
                'consumer_secret',
                'access_token_key',
                'access_token_secret'):
        with open(key, 'r') as token:
            secrets[key] = token.readline()
        # Trim the newline off
        secrets[key] = secrets[key][:-1]
    api = twitter.Api(**secrets)

if __name__ == '__main__':
    main()
