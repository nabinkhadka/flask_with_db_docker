import logging as log
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)


@app.route("/users", methods=["GET"])
def list_users():
    log.info(f"called /users")
    user_list = [{'id': 1, 'name': "nabin", 'email': "nabin@gmail.com"}]
    log.info(f"called users=>{user_list}")
    return jsonify(user_list)


# Start the app in debug mode
app.run(host="0.0.0.0", port=5000, debug=True)

