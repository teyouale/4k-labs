from flask import Blueprint,request,jsonify,make_response,render_template,current_app
import random,string
from .. import *

web = Blueprint('web',__name__,template_folder="../templates",static_folder="../static")




@web.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template('index.html')


