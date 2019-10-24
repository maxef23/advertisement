from app import app, db
from app.utils import get_user_id_by_token, get_user_by_token, login_required

from flask import jsonify
from flask import Response, request

import datetime

from app.model.UserModel import User
from app.dao import daoPool


@app.route('/login', methods=['POST'])
def login():
    in_login = request.form['login']
    in_password = request.form['password']
    current_user = User.query.filter_by(login=in_login).first()
    if current_user is None or not current_user.password == in_password:
        return Response('Логин или пароль не верны', status=406)
    else:
        return jsonify({'token': current_user.generate_auth_token().decode('utf-8')})
