
import enum
import json
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import create_engine,Column,Integer,String,TEXT,Boolean,Float,DECIMAL,DATE,Date,DateTime,Time,Text
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from app import db

class UserEntity(db.Model):
    __tablename__ = 'ai_user'
    id = Column(Integer,primary_key=True,autoincrement=True,comment='id唯一值')
    userName = Column(String(50),nullable=False,unique=True,comment='用户名')
    password = Column(String(50),nullable=False,comment='密码')
    email = Column(String(100), nullable=True,comment='邮箱')
    phone = Column(String(20),nullable=True,comment='手机号码')
    create_time = Column(DateTime,default=datetime.now,comment='创建时间')
    update_time = Column(DateTime,default=datetime.now,onupdate=datetime.now,comment='更新时间')

    def get_data_Json(data):
        return {
            'id':data.id,
            'userName':data.userName,
            'email':data.email,
            'phone':data.phone,
            'create_time':str(data.create_time),
            'update_time':str(data.update_time)
        }