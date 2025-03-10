#!/usr/bin/python3
""" module holds app """
from os import getenv
from flask import Flask, jsonify, Blueprint, make_response
from models import storage
from api.v1.views import app_views
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def tear(self):
    """ tear method """
    storage.close()


@app.errorhandler(404)
def not_found(err):
    """404 status"""
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    host = getenv("HBNB_API_HOST") or '0.0.0.0'
    port = getenv("HBNB_API_PORT") or '5000'
    app.run(host=host, port=port, threaded=True)
