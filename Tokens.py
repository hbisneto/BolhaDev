## Tokens
## Setup and connect you Twitter account here!
# Note: DO NOT share your tokens
## You can generate and regenerate tokens on Twitter Developer Platform

import tweepy
from tweepy import OAuthHandler

## API Key and API Key Secret
ConsumerKey = str('')
ConsumerSecret = str('')

## Access Token and Access Token Secret
AccessToken = str("")
AccessTokenSecret = str("")

## Authorization
Auth = tweepy.OAuthHandler(ConsumerKey, ConsumerSecret)
Auth.set_access_token(AccessToken, AccessTokenSecret)

## Create an API Object
Twitter = tweepy.API(Auth, wait_on_rate_limit = True)