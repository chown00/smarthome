from flask import Flask, render_template
from flask_socketio import SocketIO, emit

def create_app(test_config=None):
    ''' Create and configure Flask application. '''
    app = Flask(__name__)
    app.config.from_mapping(SECRET_KEY='dev')
    socketio = SocketIO(app)

    @app.route('/')
    def home():
        ''' Create homepage. '''
        return render_template('home.html.j2')

    # Get ledState from javascript client and broadcast
    @socketio.on('ledState')
    def handle_message(ledState):
        ''' 
        Handle message containing the next led state from frontend
        client. 
        '''
        # This will go out to all clients contrary to a normal emit()
        socketio.emit('broadcastLEDState', ledState)

    return app