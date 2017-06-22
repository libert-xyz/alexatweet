import logging
import os
import json, requests
import twitter

CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')


def get_api(tokens):
    token = tokens.split(',')
    api = twitter.Api(consumer_key=CONSUMER_KEY,
                      consumer_secret=CONSUMER_SECRET,
                      access_token_key=token[0],
                      access_token_secret=token[1])
    return api


def get_followers(twitterToken):

    #create api instance

    api = get_api(twitterToken)
    try:
        #Get User ID
        uId = api.VerifyCredentials()
        return uId.followers_count
    except:
        return 'Error'

def get_following(twitterToken):

    #create api instance
    api = get_api(twitterToken)
    try:
        #Get User ID
        uId = api.VerifyCredentials()

        return uId.friends_count
    except:
        return 'Error'

def tweetCount(twitterToken):

    #create api instance
    api = get_api(twitterToken)
    try:
        #Get User ID
        uId = api.VerifyCredentials()
        return uId.statuses_count
    except:
        return 'Error'

def creationDate(twitterToken):

    #create api instance
    api = get_api(twitterToken)


    #Get User ID
    try:
        uId = api.VerifyCredentials()
        creation = uId.created_at
        #return u'Mon Sep 21 23:12:13 +0000 2009'
        dateString = creation.split()

        #serialize return
        s = dateString[1] + " " + dateString[2] + " " + dateString[5]
        formatDate = str(s)

        return formatDate
    except:
        return 'Error'
