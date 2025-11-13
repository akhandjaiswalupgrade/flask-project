from flask import Blueprint, jsonify


userlogin = Blueprint ('users', __name__) 

@userlogin.route('/users')
def users():
    return jsonify(["Shiv", "Akhand", "Jordan"])


