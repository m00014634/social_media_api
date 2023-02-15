from flask import Blueprint,request
from flask_restx import Resource,Api,fields
from database.models import Post
from datetime import datetime
from werkzeug.datastructures import FileStorage # For files
from werkzeug.utils import secure_filename
import os


# Registration swagger
bp = Blueprint('posts',__name__,url_prefix='/posts')
api = Api (bp)

# to work with files
upload_parser = api.parser()
upload_parser.add_argument('file',location = 'files',type = FileStorage)



# Creating model for testing post
upload_parser.add_argument('header',type = str)
upload_parser.add_argument('main_text',type = str)
upload_parser.add_argument('user_id',type = int)


post_model = api.parser()
post_model.add_argument('new_header',type = str,required = True)
post_model.add_argument('new_main_text',type=str,required = True)

@api.route('/post')
class GetAllPostsOrCreate(Resource):
    def get(self): #Get all posts
        all_posts = Post.query.all()

        if all_posts:
            result = [{'post_id':i.id,'header':i.header,'main_text':i.main_text,'publish_date':str(i.publish_date),'user_id':i.user_id,'post_likes':i.post_likes} for i in all_posts]
            return {'status':1,'message':result}

        return {'status':0,'message':'Постов пока нет'}

    @api.expect(upload_parser)
    def post(self): #Create Post
        response = upload_parser.parse_args()
        post_image = response.get('file')
        header = response.get('header')
        main_text= response.get('main_text')
        user_id = response.get('user_id')
        publish_date = datetime.now()

        try:
            filename = secure_filename(post_image.filename)
            post_image.save(os.path.join('media/',filename))

            Post().create_post(header,main_text,publish_date,user_id,filename)
            return {'status':1,'message':'Пост успешно добавлен'}

        except:
            return {'status': 0, 'message':'Ошибка в данных'}


@api.route('/<int:post_id>')
class GetOrChangeOrDeletePostById(Resource):
    def get(self,post_id): # get exact post
        current_post = Post.query.get_or_404(post_id)
        if current_post:
            return {'status':1,'post':{'header':current_post.header,
                                       'main_text':current_post.main_text,
                                       'publish_date':str(current_post.publish_date)}}

        return {'status':0,'message':'Пост не найден'}

    @api.expect(post_model)
    def put(self,post_id): # change exact post
        args = post_model.parse_args()
        new_header = args.get('new_header')
        new_main_text = args.get('new_main_text')
        Post().change_header(post_id,new_header)
        Post().change_main_text(post_id,new_main_text)
        return {'status':1,'message':'Заголовок и описание успешно изменены'}



    def delete(self,post_id): # delete exact post
        current_post = Post.query.get_or_404(post_id)

        if current_post:
            Post.delete_post(current_post,post_id)
            return {'status':1,'message':'Пост успешно удален'}

        return {'status':0,'message':'Пост не удален'}
