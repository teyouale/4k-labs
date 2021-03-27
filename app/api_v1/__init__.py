from flask import Blueprint,request,jsonify,make_response,render_template,current_app
import random,string
from .. import *

api_v1 = Blueprint('api',__name__)




def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

from . import routes

'''
Create a new team member 
this task is given to the Amin role only
'''

