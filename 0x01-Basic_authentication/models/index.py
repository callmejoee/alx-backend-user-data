#!/usr/bin/env python3

from flask import Blueprint, abort

app_views = Blueprint('app_views', __name__)

@app_views.route('/api/v1/status', methods=['GET'])
def status():
    return jsonify({"status": "OK"})

@app_views.route('/api/v1/unauthorized', methods=['GET'])
def unauthorized():
    abort(401)

