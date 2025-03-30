from flask_socketio import SocketIO, emit
from flask import request
from database import db
from models import Message

socketio = SocketIO()

@socketio.on('send_message')
def handle_message(data):
    message = Message(sender_id=data['sender_id'], content=data['content'])
    db.session.add(message)
    db.session.commit()
    emit('receive_message', {'sender_id': data['sender_id'], 'content': data['content']}, broadcast=True)
