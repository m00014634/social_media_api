from flask import Blueprint,request
from flask_restx import Resource,Api,fields
from database.models import User

bp = Blueprint('users',__name__,url_prefix='/users')

# Регистрация как свагер
api = Api(bp)

# Model registration on swagger
user_model = api.model('user_creation',{'username':fields.String,'first_name':fields.String,
                                        'last_name':fields.String,'email':fields.String,
                                        'phone_number':fields.String,'about':fields.String})

user_model_two = api.parser()
user_model_two.add_argument('new_username',type = str,required=True)
user_model_two.add_argument('new_phone_number',type = str,required=True)
user_model_two.add_argument('new_email',type = str,required=True)
user_model_two.add_argument('new_about',type = str,required=True)


@api.route('/user')
class GetAllUsersOrCreate(Resource):
    def get(self): #Get all users
        all_users = User.query.all()
        if all_users:
            result = [{i.id: i.username} for i in all_users]
            return {'status': 1, 'users':result}
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

        try:
            User().registration(username=username, first_name=first_name, last_name=last_name, email=email,
                            phone_number=phone_number, about=about)
            return {'status':1,'message':'Польватель успешно создан'}
        except:
            return {'status':0,'message':'Этот номер уже существует'}

@api.route('/<int:user_id>')
class GetOrChangeExactUser(Resource):
    def get (self,user_id): # get exact user
        current_user = User.query.get_or_404(user_id)

        if current_user:
            return {'status':1,'user':{'username':current_user.username,
                                       'first_name':current_user.first_name,
                                       'last_name':current_user.last_name,
                                        'email':current_user.email,
                                        'phone_number':current_user.phone_number,
                                        'about':current_user.about}}

        return {'status':0,'message':'Пользователь не найден'}

    @api.expect(user_model_two)
    def put(self, user_id):
        args = user_model_two.parse_args()
        new_username = args.get('new_username')
        new_phone_number = args.get('new_phone_number')
        new_email = args.get('new_email')
        new_about = args.get('new_about')
        User().change_username(user_id, new_username)
        User().change_phone_number(user_id,new_phone_number)
        User().change_email(user_id,new_email)
        User().change_about(user_id,new_about)

        return {'status': 1, 'message': 'Данные пользователя успешно изменены'}






