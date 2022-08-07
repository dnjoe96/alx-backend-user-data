#!/usr/bin/env python3
""" Flask App Module """
from flask import Flask, jsonify, request
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'])
def index():
    """ Index view function """
    return jsonify({'message': 'Bienvenue'})


@app.route('user', methods=['POST'], strict_slashes=False)
def users():
    """ Register User"""
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        AUTH.register_user(email, password)
        return jsonify({
            'email': email,
            'message': 'user created',
        }), 200
    except ValueError:
        return jsonify({
            'message': 'email already registered'
        }), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
