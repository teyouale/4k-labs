from . import api_v1,current_app
from . import db_operations,id_generator
from flask import request,jsonify,send_from_directory,make_response,send_file
import secrets
from werkzeug.utils import secure_filename
import os
import time
from . import *
'''
create decoretors to store user infromation
'''

'''
this are used for debuging will be removed during production
'''
# @api_v1.after_request
# def after_request(response):
#     print(request.referrer)
#     response.headers.add("Access-Control-Allow-Origin", request.referrer);
#     response.headers.add("Access-Control-Allow-Methods", "GET,HEAD,OPTIONS,POST,PUT");
#     response.headers.add("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept, Authorization");
#     return response


@api_v1.route('/api_v1/delete_all_tokens')
def delete_all_tokens():
    db_operations._deleteTokens()
    return "succesully deleted all tokens"

@api_v1.route('/api_v1/delete_all_memebers')
def delete_all_memebers():
    db_operations._deleteMembers()
    return "succesully deleted all Members"

@api_v1.route('/api_v1/deleteall')
def deleteall():
   return db_operations._delteAll()

'''
    TokeGenerator
    generate Token with Division
'''


@api_v1.route('/api_v1/generate_token',methods=['POST'])
def generate_token():
    req = request.get_json()
    token = secrets.token_urlsafe()
    res = db_operations._storeToken(str(token),str(req['Division']))
    return res

#  list all the generated tokens
@api_v1.route('/api_v1/list_tokens')
def list_tokens():
    return db_operations._listToken()
    
@api_v1.route('/api_v1/delete_token/<token>')
def delete_token(token):
    return db_operations._deleteToken(str(token))

'''
    To register only username,password Full Name and Token are needed
'''


@api_v1.route('/api_v1/register_member',methods=['POST'])
def register_member():
    req = request.get_json()

    if not req:
        msg = {"message":"invalid input"}
        return jsonify(msg),400
    if not (req.get('username',None) and req.get('password',None) and req.get('fullname',None) and req.get('token',None)):
        msg = {"message":"all information is not provided"}
        return jsonify(msg),400
    data = {
        'profile_picture':'',
        'Discription':'',
        'Linkden':'',
        'Github':'',
        'Role':0,
        'Division':'',
        'projects':None,
        'username':req.get('username'),
        'password':req.get('password'),
        'fullname':req.get('fullname'),
        'token':req.get('token')
    }
    return db_operations._register_member(data)


@api_v1.route('/api_v1/members')
def list_memebers():
    return db_operations._list_members()

@api_v1.route('/api_v1/members/<user_id>')
def member(user_id):
    return db_operations._member_information(str(user_id))

'''
Delete a memeber 
        req = {
                "user_id":"BWQ8GQ9CGCOA"
              }
            
'''
@api_v1.route('/api_v1/delete_member',methods=['POST'])
def delete_member():
    req = request.get_json()
    return db_operations._delete_member(str(req['user_id']))


'''
do LOGIN here
'''

@api_v1.route('/api_v1/login',methods=['POST'])
def login():
    req = request.get_json()
    if not req:
        msg = {"message":"invalid input"}
        return jsonify(msg),400
    if not req.get('username') or len(req.get('password'))<1:
        msg = {"message":"invalid input"}
        return jsonify(msg),400
    data,passed = db_operations._check_username_password(req)
    if passed==True:
        additional_claims = data
        access_token = create_access_token(identity=data['user_id'],additional_claims=additional_claims)
        return jsonify(access_token=access_token,user= data,logged=True),200
    else:
        return data,404
'''
    TODO:
        [] make sure first if the user is logged in before updating any information
        [x] username must be sent or loaded from the information
        [] make sure the user name is taken form session 

'''
@api_v1.route('/api_v1/<user_id>/upadate_infromation',methods=['PUT'])
def update_information(user_id):
    req = request.get_json(force=True)
    subset = ['username','Linkden','Github','fullname','Discription','newpassword','password','image','user_id']
    data = {}
    for key,value in req.items():
        if key in subset and len(value):
            data[key] = value
    return db_operations._update_information(data,str(user_id))


'''
  req =   {
            "user_id":"{user id of the memember}",
            "Role":"2"
        }

'''

@api_v1.route('/api_v1/changeRole',methods=['PUT'])
def changeRole():
    req = request.get_json()
    return db_operations._change_role(req)


@api_v1.route('/api_v1/changeDivision',methods=['POST'])
def changeDivision():
    divisions = ["DEVS",'BOTS','THINGS']
    req = request.get_json()
    if not req:
        msg = {'message':'invalid request'}
        return jsonify(msg),400
    if req.get('user_id',None)==None or req.get('division',None)==None:
        msg = {'message':'invalid request'}
        return jsonify(msg),400
    if req.get('division') not in divisions:
        msg = {'message':'invalid Division'}
        return jsonify(msg),400
    return db_operations._change_division(req)

'''
    TODO:
        [x] application Form
            [x] applicarion form
            [x] sending resume or cv
            [x] make sure there is no duplicates
            
            
    the form contains
        Email Address
        FUll Name
        Acadamic level
        cv/resume
        phonenumber
        github (optional)
'''



@api_v1.route('/api_v1/sendApplication',methods=['POST'])
def sendApplication():
    data = request.form.to_dict()
    data ['suggestion'] = []
    # make sure if the path is created
    if not (os.path.exists(current_app.config['CV_PATH'])):
        os.mkdir(current_app.config['CV_PATH'])
    # check if the given name is acceptable
    file = request.files['file']
    extention = file.filename.split('.')[-1]
    generated_id = id_generator(4)
    if extention in current_app.config['ALLOWED_EXTENSIONS']:
        filename = data['FUll Name'].split(' ')[0]+generated_id
        path = os.path.join(current_app.config['CV_PATH'],filename+'.'+extention)

        #  check if there is duplication before
        while path in os.listdir(current_app.config['CV_PATH']):
            generated_id = id_generator(3)
            filename = data['FUll Name'].split(' ')[0]+generated_id
            path = os.path.join(current_app.config['CV_PATH'],filename+'.'+extention)
        # add it to dictionary and download it

        # file.save(path)
        data['path'] = path
        data['id'] = generated_id
        return db_operations._submit_application(data)
    else:
        msg = {"message":"unknow internal server error"}
        return jsonify(msg),500

'''
    donwload the cv that has been uploaded
    TODO:
        [] the download is not working

'''

@api_v1.route('/api_v1/cv/<filename>')
def download_cv(filename):
    print()
    return send_from_directory(current_app.config['CV_PATH'],filename,as_attachment=True)


'''
    List all the applicants
    this will be displayed for the admin and teamleaders only
    TODO:
        [] deleting the applicant information is not that neccessay but must be done at the futre
        [] use the path as a uniqe key 
'''
@api_v1.route('/api_v1/see_applicants')
def seeApplicants():
    return db_operations._get_applicants()

# suggest an applicant this is opetional the Team leader has an option to add this information or leave 
#  it as it is

@api_v1.route('/api_v1/add_suggestion',methods=['POST'])
def add_suggestion():
    req = request.get_json()
    return  db_operations._add_suggestion(req)

'''
    delete all the applicants used for debuging
'''

@api_v1.route('/api_v1/delete_all_applicanats')
def delete_all_applicanats():
    db_operations._delete_all_applicanats()
    return  "all the applications are delted succesfully"

'''
    Projects
        [] create Project
        [] member can submit subtask if they are only the member of the projec update Project
        [] read_Projects in detail and documentation
        [] view specific project
    schema

        project
            {
                '_id':'given by mobgodb',
                'project id':-> this is randomly generated and make sure there is no duplicate
                'project name':->given from the user,
                'subtasks':->
                'Division':->from the Team Leader who created the project
                'team members':->[array of user_id],
                'github'
                'google docks'
            }

        subtask 
        {
            '_id', given by the mongo
            'sub task': ->given from the user
            'project id',
            'finished':false
        }
'''

@api_v1.route('/api_v1/create_new_project',methods=['POST'])
def create_new_project():
    req = request.get_json()
    return db_operations._create_project(req)

@api_v1.route('/api_v1/get_projects')
@jwt_required(locations=["headers"])
def get_projects():
    return db_operations._get_all_projects()


@api_v1.route('/api_v1/get_projects/<project_code>')
@jwt_required(locations=["headers"])
def get_project(project_code):
    return db_operations._get_project(project_code)

@api_v1.route('/api_v1/project/updatemembers',methods=['POST'])
def update_project_members():
    req = request.get_json()
    if req == None:
        return jsonify("invalid request"),400
    elif req.get('project_code',None) == None:
        return jsonify(msg="please provide a valid project code"),400
    if req.get('team_members',None) == None or len(req.get('team_members')) == 0:
        return jsonify(msg="no team member is provided please provide at least one"),400
    return db_operations._update_project_members(req)

'''
    on every update of project task
'''

'''
    delete project 
    also deltes all the subtasks of the project
'''
@api_v1.route('/api_v1/delete_project/<project_code>')
def delete_project(project_code):
    return db_operations._delete_project(project_code)

'''
    update project tittle,github link,docks link,Description
'''

@api_v1.route('/api_v1/updateproject',methods=['POST'])
def update_project():
    req = request.get_json()
    if not req:
        msg = {'message':'invalid input'}
        return jsonify(msg),400
    if not req.get('project_code',None):
        msg = {'message':'invalid input'}
        return jsonify(msg),400
    return db_operations._update_project(req)


@api_v1.route('/api_v1/completeTask', methods = ['PUT'])
def completeTask():
    req = request.get_json()
    if not req:
        msg = {"message":"task code is not provided"}
        return jsonify(msg),400
    return db_operations._completeTask(str(req.get('task_code')))
    
    
@api_v1.route('/api_v1/addTask', methods = ['POST'])
def addTask():

    req = request.get_json()
    #  if it is none
    if not req:
        msg = {"message":"invalid input"}
        return jsonify(msg),400
    
    if not req.get('project_code') or len(req.get('task'))<1:
        msg = {"message":"invalid input"}
        return jsonify(msg),400
    return db_operations._addTask(req)

'''
delete a task 
'''

@api_v1.route('/api_v1/deleteTask/<task_code>', methods = ['POST'])
def deleteTask(task_code):
    return db_operations._deleteTask(task_code)

@api_v1.route('/api_v1/renameTask', methods = ['POST'])
def renameTask():
    req = request.get_json()
    #  if it is none
    if not req:
        msg = {"message":"invalid input"}
        return jsonify(msg),400
    if not req.get('task_code') or len(req.get('task'))<1:
        msg = {"message":"invalid input"}
        return jsonify(msg),400
    return db_operations._rename_task(req)

@api_v1.route('/api_v1/renameProject', methods = ['POST'])
def renameProject():
    req = request.get_json()
    #  if it is none
    if not req:
        msg = {"message":"invalid input"}
        return jsonify(msg),400
    if not req.get('project_code') or len(req.get('project title'))<1:
        msg = {"message":"invalid input"}
        return jsonify(msg),400
    return db_operations._rename_project(req)

@api_v1.route('/api_v1/get_profile/<image>')
def get_image(image):
    profile_path = current_app.config['PROFILE_PICTURES']

    path = os.path.join(os.getcwd(),profile_path,image)

    if os.path.exists(path):
        return send_file(path, mimetype='image/jpg')
    return jsonify({'message':"file doesn't exist"}),404

@api_v1.route('/api_v1/get_thumbnail/<image>')
def get_thumbnail(image):
    thumbnail_path = current_app.config['THUMBNAILS']

    path = os.path.join(os.getcwd(),thumbnail_path,image)

    if os.path.exists(path):
        return send_file(path, mimetype='image/jpg')
    return jsonify({'message':"file doesn't exist"}),404



