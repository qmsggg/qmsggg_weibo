# -*- coding: utf-8 -*-

import flask
from flask import request, redirect, flash, render_template, url_for, jsonify
from application.extensions import session
from application.models import User

user_manager_bp = flask.Blueprint(
    'user_manager',
    __name__,
    template_folder='../templates'
)


@user_manager_bp.route('/user/register', methods=['POST'])
def user_register():
    _form = request.form

    if request.method == 'POST':
        user_name = _form["user_name"]
        passwd = _form["passwd"]
        user = User(user_name=user_name, passwd=passwd)
        try:
            user.store()
            flash("register successfully!")
            return jsonify({'user_name': user_name, 'success': 0, 'message': "register successfully!"})
        except Exception as e:
            print(e)
            flash("register failed!")
            return jsonify({'user_name': "", 'success': 1, 'message': "register failed!"})
    return jsonify({'user_name': "", 'success': 1, 'message': "not support methods!"})