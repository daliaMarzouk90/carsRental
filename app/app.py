from flask import Flask, render_template
from datetime import datetime

from car import carApp
from customer import customerApp

def registerModules(app):
    app.register_blueprint(customerApp)
    app.register_blueprint(carApp)

def initApp():
    app = Flask(__name__)
    app.secret_key = "APP-SECRET-KEY"
    return app



app = initApp()

@app.route('/')
def index():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

registerModules(app)