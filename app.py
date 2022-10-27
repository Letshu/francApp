from flask import Flask, render_template, jsonify, Response, request
from sqlalchemy import null, true
from jinja2 import Environment,FileSystemLoader
import getTweets

app = Flask(__name__)

@app.route('/')
def index_view():
    username = request.args.get('username')
    return render_template('index.html', username = username)

@app.route('/users')
def users_view():
    with open('./users.json', 'r') as f:
        users = f.read()
    return Response(users, mimetype="application/json")

@app.route('/posts')
def posts_view():
    with open('./posts.json', 'r') as f:
        posts = f.read()
    return Response(posts, mimetype="application/json")

@app.route('/william')
def william_tweets_followers():
    data = getTweets.getUserTweets("WilliamLetchu")
    tweets = []
    for tweet in data:
        tweets.append(tweet.text)
    followers = getTweets.getUserFollower("WilliamLetchu")
    print(followers)
    return render_template('users.html',tweets=tweets, followers=followers)


if __name__ == '__main__':
    app.run(host='127.0.0.1',debug=true)