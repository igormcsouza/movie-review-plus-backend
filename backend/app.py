from flask import Flask
import config

app = Flask(__name__)
app.config.from_object(config)

from flask_restful import Api
from resources import MovieReviewPredict

api = Api(app)
api.add_resource(MovieReviewPredict, '/movie-review-predict')


