from flask import Flask
from db import db
from flask_restful import Api
from restaurant_routes import Restaurants, RestaurantMember
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///data.db")
api = Api(app)
@app.before_first_request
def create_tables():
  db.create_all()

# @app.route("/")
# def home():
#   return "hello world!"

api.add_resource(Restaurants, "/restaurants")
api.add_resource(RestaurantMember, "/restaurants/<id>")

db.init_app(app)
if __name__ == "__main__":
    app.run(port=5000)
#   app.run(host="0.0.0.0", port=5000)
