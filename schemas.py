# schemas.py
from wsgi import ma
from models import Tweet, User

class TweetSchema(ma.Schema):
    class Meta:
        model = Tweet
        fields = ('id', 'text', 'created_at')

tweet_schema = TweetSchema()
tweets_schema = TweetSchema(many = True)

class UserSchema(ma.Schema):
    class Meta:
        model = User
        fields = ('id', 'username', 'api_token')

user_schema = UserSchema()
users_schema = UserSchema(many = True)
