from flask import Blueprint,request
from flask_restx import Resource,Api,fields
from database.models import User

bp = Blueprint('users',__name__,url_prefix='/user')

# Регистрация как свагер
api = Api(bp)

# Model registration on swagger
user_model = api.model('user_creation',{'username':fields.String,'first_name':fields.String,
                                        'last_name':fields.String,'email':fields.String,
                                        'phone_number':fields.String,'about':fields.String})


@api.route('/')
class GetAllUsersOrCreate(Resource):
    def get(self): #Get all users
        all_users = User.query.all()
        if all_users:
            result = [{i.id: i.username} for i in all_users]
            return result
        return []
    @api.expect(user_model)
    def post(self): #Registration user
        response = request.json

        username = response.get('username')
        first_name = response.get('first_name')
        last_name = response.get('last_name')
        email = response.get('email')
        phone_number = response.get('phone_number')
        about = response.get('about')

        User().registration(username=username, first_name=first_name, last_name=last_name, email=email,
                        phone_number=phone_number, about=about)

        return {'status':1,'message':'Польватель успешно создан'}

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

