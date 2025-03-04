import jwt
from datetime import datetime, timedelta

from app import redis_client

from entity.orm.User import UserEntity

def query_user_Info(userName,password):
    try:

        user = UserEntity.query.filter(UserEntity.userName == userName,UserEntity.password == password).first()

        if user != None:
            data = UserEntity.get_data_Json(user)
            payload = {
                'id':data['id'],
                'exp': datetime.utcnow() + timedelta(days=0, seconds=600)
            }

            token = jwt.encode(payload,data['userName'], algorithm='HS256')

            # print(token)
            data['token'+str(data['id'])] = token
            redis_client.setex('token'+str(data['id']),40,token)

            print(data)
            return {
                'code':200,
                'data':data,
                'msg':'获取用户信息成功'
            }
        else:
             return {
                'code':-1,
                'msg':'用户不存在'
            }

        
        # print(user)
    except Exception as e:
        print(e)
        return {
            'code':-1,
            'msg':'获取用户信息失败'
        }