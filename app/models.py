#app/models.py
from datetime import datetime
from app import create_app

# class Tweet:
#     def __init__(self, text):
#         self.text = text
#         self.created_at = datetime.now()
#         self.id = None

class Tweet(db.Model):
    __tablename__ = "tweets"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String())
    created_at = db.Column(db.datetime.now())

    def __repr__(self):
        return '<id {}>'.format(self.id)
