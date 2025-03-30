from flask import Flask, request, jsonify
from database import db
from models import User, Message
from flask_cors import CORS
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config.from_object('config.Config')
db.init_app(app)
CORS(app)
bcrypt = Bcrypt(app)

@app.route('/api/register', methods=['POST'])
def register():
    data = request.json
    user = User(username=data['username'], fio=data['fio'], phone=data['phone'])
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'Пользователь зарегистрирован'})

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()
    if user and user.check_password(data['password']):
        return jsonify({'message': 'Успешный вход', 'user_id': user.id})
    return jsonify({'message': 'Ошибка входа'}), 401
