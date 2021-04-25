from flask import Blueprint,request,jsonify,make_response,render_template,current_app
import random,string
from .. import *

web = Blueprint('web',__name__,template_folder="../templates",static_folder="../static")


@web.route('/')
def index():
    return render_template('index.html')


@web.route('/login')
def login():
    return render_template('index.html')

@web.route('/app', defaults={'path': ''})
@web.route('/app/<path:path>')
def catch_all(path):
    return render_template('index.html')



@web.route('/admin', defaults={'path': ''})
@web.route('/admin/<path:path>')
def catch_all2(path):
    return render_template('index.html')


