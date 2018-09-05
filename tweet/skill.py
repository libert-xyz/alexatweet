import logging
import os

from flask import Flask, render_template
from flask_ask import Ask, request, session, question, statement
from twiteerApi import get_followers, get_following, tweetCount, creationDate

app = Flask(__name__)
ask = Ask(app, "/")

log = logging.getLogger()
log.addHandler(logging.StreamHandler())
log.setLevel(logging.DEBUG)
logging.getLogger('flask_ask').setLevel(logging.DEBUG)
auth_url = 'https://tweeter-info-oauth.herokuapp.com/authorize'

@ask.launch
def launch():
    if session.user.get('accessToken') == None:
        link_account_response = render_template('link_acct')
        return statement(link_account_response) \
            .link_account_card()
    welcome = render_template('welcome')
    print session.user.accessToken
    return question(welcome)


@ask.intent('FollowersIntent')
def followers():
    if session.user.get('accessToken') == None:
        link_account_response = render_template('link_acct')
        return statement(link_account_response) \
            .link_account_card()
    count = get_followers(session.user.accessToken)
    if count == 'Error':
        error_response = render_template('error_temp')
        return statement(error_response)
    followers = render_template('followers',count=count)
    return question(followers) \
        .standard_card(title='Followers...',
        text=followers,
        small_image_url='https://pbs.twimg.com/app_img/877655491240919040/EBqe8Bvh?format=jpg&name=73x73')


@ask.intent('FollowingsIntent')
def followings():
    if session.user.get('accessToken') == None:
        link_account_response = render_template('link_acct')
        return statement(link_account_response) \
            .link_account_card()
    count = get_following(session.user.accessToken)
    if count == 'Error':
        error_response = render_template('error_temp')
        return statement(error_response)
    followings = render_template('followings',count=count)
    return question(followings) \
        .standard_card(title='Friends...',
        text=followings,
        small_image_url='https://pbs.twimg.com/app_img/877655491240919040/EBqe8Bvh?format=jpg&name=73x73')

@ask.intent('NumberOfTweetsIntent')
def number_of():
    if session.user.get('accessToken') == None:
        link_account_response = render_template('link_acct')
        return statement(link_account_response) \
            .link_account_card()
    count = tweetCount(session.user.accessToken)
    if count == 'Error':
        error_response = render_template('error_temp')
        return statement(error_response)
    tweet = render_template('tweets',count=count)
    return question(tweet) \
        .standard_card(title='Number of Tweets...',
        text=tweet,
        small_image_url='https://pbs.twimg.com/app_img/877655491240919040/EBqe8Bvh?format=jpg&name=73x73')

@ask.intent('AccountDateIntent')
def account_date():
    if session.user.get('accessToken') == None:
        link_account_response = render_template('link_acct')
        return statement(link_account_response) \
            .link_account_card()

    count = creationDate(session.user.accessToken)
    if count == 'Error':
        error_response = render_template('error_temp')
        return statement(error_response)
    account = render_template('accountDate',count=count)
    return question(account) \
        .standard_card(title='Account creation date...',
        text=account,
        small_image_url='https://pbs.twimg.com/app_img/877655491240919040/EBqe8Bvh?format=jpg&name=73x73')

@ask.intent('StopIntent')
def stop_intent():
    stop = render_template('stop')
    return statement(stop)

@ask.intent('NoIntent')
def no_intent():
    no_template = render_template('no_reponse')
    return statement(no_template)

@ask.intent('YesIntent')
def yes_intent():
    yes_template = render_template('yes_response')
    return question(yes_template)

@ask.intent('HelpIntent')
def help_intent():
    help_template = render_template('help')
    return question(help_template)

@ask.intent('CancelIntent')
def cancel_intent():
    cancel_template = render_template('cancel_response')
    return statement(cancel_template)


if __name__ == '__main__':
    app.run(debug=True)
