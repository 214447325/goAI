from flask import Flask

import os

import redis

from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate


app = Flask(__name__)


HOSTNAME = os.getenv('SQLHOST')

PORT = os.getenv('SQLPORT')

USERNAME = os.getenv('SQLUSER')

PASSWORD = os.getenv('SQLPASSWORD')

DATABASE = os.getenv('SQLDATABASE')

DB_URL =f"mysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8"

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL  # 配置数据库 URI

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

migrate = Migrate(app,db)

REDIShOST = os.getenv('REDIShOST')

REDIShPORT = os.getenv('REDIShPORT')

REDISDB = os.getenv('REDISDB')

REDISPASSWORD = os.getenv('REDISPASSWORD')

redis_client = redis.StrictRedis(host=REDIShOST, port=REDIShPORT, db=REDISDB,password=None, decode_responses=True)

# import entity.

import entity.Entity

from routers.UserRouter import userRouter

app.register_blueprint(userRouter)


