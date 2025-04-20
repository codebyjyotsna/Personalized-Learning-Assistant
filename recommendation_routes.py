from flask import Blueprint, request, jsonify
from models.recommendation_engine import recommend_resources

recommendation_routes = Blueprint("recommendation_routes", __name__)

@recommendation_routes.route("/recommend", methods=["POST"])
def recommend():
    data = request.json
    resources = recommend_resources(data["learning_style"])
    return jsonify({"resources": resources})
