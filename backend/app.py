from flask import Flask
from database import db
from routes import app
from sockets import socketio

app.config.from_object('config.Config')
db.init_app(app)
socketio.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
