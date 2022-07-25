from flask import Blueprint
from app.models import Review

review_routes = Blueprint('reviews', __name__)

@review_routes.route('/')
def reviews():
  reviews = Review.query.all()
  print(reviews)
  return {'reviews': [review.to_dict() for review in reviews]}
