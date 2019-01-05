# -*- coding: utf-8 -*-

import flask
from flask import request, redirect, flash, render_template, url_for
from application.extensions import db
from application.models import UserInfo

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
        user = UserInfo(user_name=user_name, passwd=passwd)
        try:
            user.store()
            flash("register successfully!")
            return {user_name}
        except Exception as e:
            print(e)
            flash("register failed!")