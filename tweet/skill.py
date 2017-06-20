import logging
import os

from flask import Flask, render_template
from flask_ask import Ask, request, session, question, statement


app = Flask(__name__)
ask = Ask(app, "/")

log = logging.getLogger()
log.addHandler(logging.StreamHandler())
log.setLevel(logging.DEBUG)
logging.getLogger('flask_ask').setLevel(logging.DEBUG)


@ask.launch
def launch():
    welcome = render_template('welcome')
    return question(welcome)


@ask.intent('FollowersIntent')
def followers():
    followers = render_template('followers')
    return question(followers)


@ask.intent('FollowingsIntent')
def followings():
    followings = render_template('followings')
    return question(followings)

@ask.intent('NumberOfTweetsIntent')
def followings():
    followings = render_template('followings')
    return question(followings)

@ask.intent('AccountDateIntent')
def account():
    account = render_template('accountDate')
    return question(account)

if __name__ == '__main__':
    app.run(debug=True)
