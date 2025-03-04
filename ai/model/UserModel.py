import jwt
from datetime import datetime, timedelta

from app import redis_client

from entity.orm.User import UserEntity

def query_user_Info(userName,password):
    try:
        
        print(userName)
        print(password)
        user = UserEntity.query.filter(UserEntity.userName == userName,UserEntity.password == password).first()
        data = UserEntity.get_data_Json(user)

        payload = {
            'id':data['id'],
            'exp': datetime.utcnow() + timedelta(days=0, seconds=600)
        }

        token = jwt.encode(payload,data['userName'], algorithm='HS256')

        print(token)
        data['token'] = token
        redis_client.setex('token',20,token)

        print(data)
        return {
            'code':200,
            'data':data,
            'msg':'获取用户信息成功'
        }
        # print(user)
    except Exception as e:
        print(e)
        return {
            'code':-1,
            'msg':'获取用户信息失败'
        }