#!/usr/bin/env python3
""" Flask App Module """
from flask import Flask, jsonify, request, abort, make_response,\
    redirect, url_for
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
    # session_id = resp.headers.get('Set-Cookie').
    # split('session_id=')[-1].split(';')[0]
    # print(resp.headers.get('Set-Cookie').
    # split('session_id=')[-1], type(resp.headers.get('Set-Cookie').
    # split('session_id=')[-1]))
    return jsonify({
        'email': email,
        'message': 'logged in',
    })


@app.route('/sessions', methods=['DELETE'])
def logout():
    """ Logout view """
    session_id = request.cookies.get('session_id')
    if session_id:
        user = AUTH.get_user_from_session_id(session_id)
        if user:
            AUTH.destroy_session(user.id)
            return redirect('/')
    abort(403)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
