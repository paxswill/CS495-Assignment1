#!/usr/bin/env python

import twitter

def post(api_handle, tweet):
    pass

def last_100(api_handle, username):
    pass

def list_hashtags(tweets):
    pass

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
