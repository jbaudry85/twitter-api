# wsgi.py
try:
    from dotenv import load_dotenv
    load_dotenv()
except:
    pass # Heroku does not use .env

from flask import Flask, request
from config import Config
app = Flask(__name__)
app.config.from_object(Config)


from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

from models import Tweet, User
from schemas import tweets_schema, tweet_schema, user_schema, users_schema

@app.route('/')
def home():
    return "Hello word"

@app.route('/api/v1/tweets')
def tweets():
    tweets = db.session.query(Tweet).all()
    return tweets_schema.jsonify(tweets)

@app.route('/api/v1/tweets/<id>')
def get_tweet(id):
    tweet = db.session.query(Tweet).get(int(id))
    return tweet_schema.jsonify(tweet)

@app.route('/api/v1/tweets', methods=['POST'])
def add_tweet():
    new_tweet = Tweet()
    new_tweet.text = request.form['text']
    new_tweet.created_at = request.form['created_at']
    db.session.add(new_tweet)
    db.session.commit()
    return tweet_schema.jsonify(new_tweet)

@app.route('/api/v1/tweets', methods=['PATCH'])
def update_tweet():
    new_tweet = Tweet()
    new_tweet.id = request.form['id']
    new_tweet.text = request.form['text']
    db.session.query(Tweet).filter_by(id=new_tweet.id).update({"text" : new_tweet.text})
    db.session.commit()
    return tweet_schema.jsonify(new_tweet)

@app.route('/api/v1/tweets/<id>', methods=['DELETE'])
def delete_tweet(id):
    db.session.query(Tweet).filter_by(id=id).delete()
    db.session.commit()
    return ('', 200)

@app.route('/api/v1/users')
def users():
    users = db.session.query(User).all()
    return users_schema.jsonify(users)

@app.route('/api/v1/users', methods=['POST'])
def add_user():
    new_user= User()
    new_user.username = request.form['username']
    db.session.add(new_user)
    db.session.commit()
    return user_schema.jsonify(new_user)
