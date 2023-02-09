from flask import Blueprint
from flask_restx import Resource,Api,fields

bp = Blueprint('users',__name__,url_prefix='/user')

# Регистрация как свагер
api = Api(bp)

@api.route('/')
class GetAllUsersOrCreate(Resource):
    def get(self): #Get all users
        pass

    def post(self): #Registration user
        pass


@api.route('/<int:user_id>')
class GetExactUser(Resource):
    def get (self,user_id): # get exact user
        pass


@api.route('/<int:photo_id>')
class ChangeOrDeleteUserPhoto(Resource):
    def put(self,photo_id): #Change
        pass

    def delete (self,photo_id): # Delete
        pass

