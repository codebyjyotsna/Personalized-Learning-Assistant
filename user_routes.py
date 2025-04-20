from flask import Blueprint, request, jsonify

user_routes = Blueprint("user_routes", __name__)

@user_routes.route("/log", methods=["POST"])
def log_interaction():
    data = request.json
    # Save user interaction data (e.g., to database)
    return jsonify({"message": "Interaction logged successfully!"})
