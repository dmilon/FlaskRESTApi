from flask_restful import Resource, reqparse
from restaurant import Restaurant
parser = reqparse.RequestParser()
parser.add_argument("name", type=str)

class Restaurants(Resource):
  def post(self):
    data = parser.parse_args()
    restaurant = Restaurant(data["name"])
    restaurant.save()
    return restaurant.json(), 201

  def get(self):
    return [r.json() for r in Restaurant.query.all()]

class RestaurantMember(Resource):
  def get(self, id):
    restaurant = Restaurant.find_by_id(id)
    if restaurant:
      return restaurant.json()
    else:
      return { "error": "Not found" }, 404

  def patch(self, id):
    restaurant = Restaurant.find_by_id(id)
    data = parser.parse_args()
    if restaurant:
      restaurant.name = data["name"]
      restaurant.save()
      return restaurant.json()
    else:
      return { "error": "Not found" }, 404

  def delete(self, id):
    restaurant = Restaurant.find_by_id(id)
    if restaurant:
      restaurant.destroy()
      return restaurant.json()
    else:
      return { "error": "Not found" }, 404
