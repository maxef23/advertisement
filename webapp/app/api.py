from app import app, db
from app.utils import get_user_id_by_token, get_user_by_token, login_required

from flask import jsonify
from flask import Response, request

import datetime

import secrets
import string

from app.model.UserModel import User
from app.dao import daoPool


# создание почтового клиента
from flask_mail import Mail,  Message
import smtplib

app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT = 465,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = 'webiraylab.advertisement@gmail.com',
    MAIL_PASSWORD = 'webiraylab.advertisement123'
)
mail = Mail(app)



@app.route('/login', methods=['POST'])
def login():
    in_login = request.form['login']
    in_password = request.form['password']
    current_user = User.query.filter_by(login=in_login).first()
    if current_user is None or not current_user.password == in_password:
        return Response('Логин или пароль не верны', status=406)
    else:
        return jsonify({'token': current_user.generate_auth_token().decode('utf-8')})


@app.route('/register', methods=['POST'])
def register():
    is_user_exist = User.query.filter_by(login=request.form['email']).first()
    if is_user_exist is not None:
        return Response('Email уже существует', status=406)
    password = ''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(8))
    msg = Message(
        'Registration',
        sender='webiraylab.advertisement@gmail.com',
        recipients=[request.form['email']],
        body="Login: " + request.form['email'] + "\n" + "Password: " + password
    )
    new_user = User(request.form['email'], password)
    daoPool.sqlDAO.session.add(new_user)
    daoPool.sqlDAO.session.commit()

    mail.send(msg)
    return 'Mail sent'



