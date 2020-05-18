from flask import Flask, render_template

def create_app(test_config=None):
    # Create and configure Flask application
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='dev')

    # Homepage
    @app.route('/')
    def home():
        return render_template('home.html.j2')

    return app