from flask import Flask, render_template
from flask_socketio import SocketIO, emit

def create_app(test_config=None):
    # Create and configure Flask application
    app = Flask(__name__)
    app.config.from_mapping(SECRET_KEY='dev')
    socketio = SocketIO(app)

    # Homepage
    @app.route('/')
    def home():
        return render_template('home.html.j2')

    @socketio.on('message')
    def handle_message(message):
        print('received message: ' + message)

    @socketio.on('add')
    def handle_add(data):
        print(data)
        data = data + 1
        emit('sum', data)

    return app