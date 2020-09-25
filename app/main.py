# random number generators
from random import seed, random, randint

# using tweepy to interact with twitter api
import tweepy

# import flask and set up app
from flask import Flask, render_template, request, redirect
app = Flask(__name__, template_folder='templates')

# access keys
CONSUMER_KEY = "19q6FoMnUt4JWXe3NfvUs1hqL"
CONSUMER_SECRET = "S6YmwcIA78DoBSTXr1CW8vxPjObzEuGXLon8zaYx3hzJuBc3iB"
ACCESS_TOKEN = "1306023029525360640-YVA5ALNsrSH1nSvQ0vUQRKeprokPYc"
ACCESS_SECRET = "KxffeClqFLe5C4xIeh31PkdqdOD8rFGZqyxy464unvvqj"

# twitter authorization
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

# lets get our api
api = tweepy.API(auth)

# example to post a tweet on our account
# api.update_status('This is a test tweet.')

# get tweets from an account
user = api.get_user('elonmusk')

# grab elon tweets
status = api.user_timeline(
    'elonmusk', include_retweets=False, include_replies=False, count=3200)

elon_arr = []
for tweetObj in status:
    if hasattr(tweetObj, 'retweeted_status'):
        continue
    if '@' or 'https' in tweetObj.text:
        continue
    else:
        elon_arr.append(tweetObj.text)

# grab kanye tweets
status = api.user_timeline(
    'kanyewest', include_retweets=False, include_replies=False, count=3200)

kanye_arr = []
for tweetObj in status:
    if hasattr(tweetObj, 'retweeted_status'):
        continue
    if '@' or 'https' in tweetObj.text:
        continue
    else:
        kanye_arr.append(tweetObj.text)

# both arrays are full of tweets

# run our game


def main():
    # where I am lost

    score = 0
    i = 0
    while i < 10:
        sendTweetToHTML()
        i = i + 1


@app.route('/')
def sendTweetToHTML():
    # we need to grab a kanye/elon by random
    # we need to grab a tweet by random
    # update html with tweet
    # keep track of what user clicks in submit
    # update score accordingly

    seed(1)
    value = 0.3
    if value < 0.5:
        tweetIndex = randint(0, len(kanye_arr) - 1)
        tweet = kanye_arr[tweetIndex]
    else:
        tweetIndex = randint(0, len(elon_arr) - 1)
        tweet = elon_arr[tweetIndex]

    # put tweet in html
    return render_template("base.html", data=tweet)


app.route('/answer', methods=['POST'])


def getUserAnswer():
    # check if null
    if request.form['elon-btn']:
        userAns = 'elon'
    else:
        userAns = 'kanye'
    return redirect('/')


if __name__ == '__main__':
    app.run()
