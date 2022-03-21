from flask import  Blueprint
from flask_cors import CORS

customerApp = Blueprint('customer', __name__,
    template_folder='templates',
    static_folder='static')

CORS(customerApp, resources=r'/')

from customer import views