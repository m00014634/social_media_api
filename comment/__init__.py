from datetime import datetime
from flask import Blueprint
from flask_restx import Resource,Api,fields
from database.models import Comment
bp = Blueprint('comments',__name__,url_prefix='/comments')
api = Api(bp)

comment_model = api.parser()
comment_model.add_argument('text',type=str,required = True)
comment_model.add_argument('post_id',type=int,required = True)

new_comment_model = api.parser()
new_comment_model.add_argument('new_text',type=str,required = True)



@api.route('/comment')
class Create(Resource):
    def get(self): # get all comments
        all_comments = Comment.query.all()
        if all_comments:
            result = [{'comment_id':i.id,'text':i.text,'likes':i.likes,'data':str(i.data),'post_id':i.post_id} for i in all_comments]
            return {'status':1,'message':result}
        return {'status':0,'message':'Пока нет комментов'}

    @api.expect(comment_model)
    def post(self): # create_comment_to_post_by_post_id
        args = comment_model.parse_args()
        text = args.get('text')
        post_id = args.get('post_id')
        data = datetime.now()
        Comment().create_comment(text,data,post_id)
        return {'status':1,'message':'Комментарий успешно добавлен'}


@api.route('/<int:post_id>')
class GetOrDeleteOrPutByPostId(Resource):
    def get(self,post_id): # read_comment_by_post_id
         current_comment = Comment.query.get_or_404(post_id)
         if current_comment:
             return {'status':1,'comment':{'text':current_comment.text,
                                           'data':str(current_comment.data)
                                           }}
         return {'status':0,'message':'Комментарий не найден'}

    @api.expect(new_comment_model)
    def put(self,post_id): # update_comment_by_post_id
        args = new_comment_model.parse_args()
        new_text = args.get('new_text')
        Comment().change_comment_text(post_id,new_text)
        return {'status':1,'message':'Комментарий успешно изменен'}



    def delete(self,post_id):  # delete_comment_from_post_by_post_id
        Comment().delete_comment(post_id)
        return {'status':1,'message':'Комментарий успешно удален'}