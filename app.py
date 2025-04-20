from flask import Flask
from routes.user_routes import user_routes
from routes.detection_routes import detection_routes
from routes.recommendation_routes import recommendation_routes

app = Flask(__name__)

# Register routes
app.register_blueprint(user_routes, url_prefix="/user")
app.register_blueprint(detection_routes, url_prefix="/detect")
app.register_blueprint(recommendation_routes, url_prefix="/recommend")

if __name__ == "__main__":
    app.run(debug=True)
