# app/__init__.py
try:
    from dotenv import load_dotenv
    load_dotenv()
except:
    pass

from flask import Flask
from config import Config

#from .db import tweet_repository
#from .models import Tweet
#tweet_repository.add(Tweet("a first tweet"))
#tweet_repository.add(Tweet("a second tweet"))

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from flask_sqlalchemy import SQLAlchemy
    db = SQLAlchemy(app)

    from .models import Tweet

    # Remove the previous code using `@app` and replace it with:
    from .main.controllers import main
    app.register_blueprint(main)

    from .api.tweets import api as tweet_api
    app.register_blueprint(tweet_api, url_prefix = "/api/v1")

    return app
