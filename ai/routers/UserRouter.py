import json
from flask import Blueprint,request

# import importlib
import model.UserModel as userModel
# from model.UserModel import query_user_Info

userRouter = Blueprint('user', __name__,url_prefix='/user')

# userModel = importlib('model.UserModel')

@userRouter.route('/login',methods=['GET'])
def login():
    userName = request.args.get('userName')
    password = request.args.get('password')
    data = userModel.query_user_Info(userName=userName,password=password)
    return json.dumps(data)
