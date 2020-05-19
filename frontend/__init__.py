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

    # Handle message from javascript client and send broadcast
    @socketio.on('message')
    def handle_message(message):
        print('received message: ' + message)
        socketio.emit('broadcast', message)     # This will go to all clients

    # Handle and send message from javascript client
    @socketio.on('add')
    def handle_add(data):
        print(data)
        data = data + 1
        emit('sum', data)

    # Handle messages from python client
    @socketio.on('client')
    def handle_client(message):
        print(message)

    return app