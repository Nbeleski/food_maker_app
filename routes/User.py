
from flask import abort
from flask_restful import reqparse, Api, Resource

from main import app, db
from models.User import User, UserSchema, user_schema, users_schema

user_request_parser = reqparse.RequestParser()
user_request_parser.add_argument('username', type=str, help='user name')
user_request_parser.add_argument('email', type=str)
user_request_parser.add_argument('password', type=str)
user_request_parser.add_argument('permissions', type=int)

class UserList(Resource):
    def get(self):
        users = User.query.all()
        return {'users': users_schema.dump(users)}

    def post(self):
        args = user_request_parser.parse_args()
        new_user = User(username=args['username'], email=args['email'], password=args['password'], permissions=args['permissions'])

        db.session.add(new_user)
        db.session.commit()

        return user_schema.dump(new_user), 201

class UserDetails(Resource):
    def get(self, username):
        user = User.query.filter_by(username=username).first()
        if user is None:
            return {'error': 'user not found'}, 404

        return user_schema.dump(user)
    
    def delete(self, username):
        deleted = User.query.filter_by(username=username).delete()
        if deleted == 0:
            return {'error': 'user not found'}, 404

        db.session.commit()
        return {'message': 'user ' + username + ' deleted'}

        
    
# @app.route('/users')
# def get_user_list():
#     # show the list of users
#     users = User.query.all()
#     return {'users': users_schema.dump(users)}


# @app.route('/users/<string:username>')
# def get_user_details(username):
#     # show the user details for that user
#     user = User.query.filter_by(username=username).first()
#     if user is None:
#         abort(404)

#     return user_schema.dump(user)