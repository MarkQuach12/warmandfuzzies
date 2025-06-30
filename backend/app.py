from flask import Flask, jsonify, request
from flask_cors import CORS
from routes.auth_routes import auth_routes
from routes.message_routes import message_routes
from routes.group_routes import group_routes

app = Flask(__name__)
CORS(app)

app.register_blueprint(auth_routes)
app.register_blueprint(message_routes)
app.register_blueprint(group_routes)

if __name__ == '__main__':
    app.run(debug=True)