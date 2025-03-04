import entity.orm.User



def token_required(f):
    pass
    # @wraps(f)
    # def decorated(*args, **kwargs):
    #     token = request.headers.get('Authorization')
    #     if not token:
    #         return jsonify({'message': 'Token is missing!'}), 403
    #     try:
    #         jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
    #     except:
    #         return jsonify({'message': 'Token is invalid!'}), 403
    #     return f(*args, **kwargs)
    # return decorated