from flask import  Blueprint
from flask_cors import CORS

carApp = Blueprint('car', __name__,
    template_folder='templates',
    static_folder='static')

CORS(carApp, resources=r'/')

from car import views