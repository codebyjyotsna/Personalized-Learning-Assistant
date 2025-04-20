from flask import Blueprint, request, jsonify
from models.learning_style_detector import predict_learning_style

detection_routes = Blueprint("detection_routes", __name__)

@detection_routes.route("/detect", methods=["POST"])
def detect_learning_style():
    data = request.json
    prediction = predict_learning_style(data["interaction_data"])
    return jsonify({"learning_style": prediction})
