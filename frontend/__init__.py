from flask import Flask, render_template
from flask_socketio import SocketIO, emit

# Test

def create_app(test_config=None):
    ''' Create and configure Flask application. '''
    app = Flask(__name__)
    app.config.from_mapping(SECRET_KEY='dev')
    socketio = SocketIO(app)

    @app.route('/')
    def home():
        ''' Home page. '''
        return render_template('home.html.j2')

    @app.route('/layout')
    def layout_view():
        ''' Page shows status of lights in graphical view. '''
        return render_template('layout.html.j2')

    @app.route('/list')
    def list_view():
        ''' Page shows status of lights in list view. '''
        return render_template('list.html.j2')

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