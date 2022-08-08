#!/usr/bin/env python3
""" Flask App Module """
from flask import Flask, jsonify, request, abort, make_response
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'])
def index():
    """ Index view function """
    return jsonify({'message': 'Bienvenue'})


@app.route('/users', methods=['POST'], strict_slashes=False)
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


@app.route('/sessions', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    if not AUTH.valid_login(email, password):
        abort(401)

    session = AUTH.create_session(email)
    resp = make_response('store session')
    resp.set_cookie('session_id', session)
    return jsonify({
        'email': email,
        'message': 'logged in',
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
