#app/models.py
from datetime import datetime
from wsgi import app, db
import uuid

# class Tweet:
#     def __init__(self, text):
#         self.text = text
#         self.created_at = datetime.now()
#         self.id = None

class Tweet(db.Model):
    __tablename__ = "tweets"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String())
    created_at = db.Column(db.String())
    #children = relationship("User")

    def __repr__(self):
        return '<id {}>'.format(self.id)

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    api_token = db.Column(db.String(), default=uuid.uuid4)
    #tweets_id = Column(Integer, ForeignKey('tweets.id'))

    def __repr__(self):
        return '<id {}>'.format(self.id)
