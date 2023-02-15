from flask import Blueprint
from flask_restx import Resource,Api,fields
from database.models import Table

bp = Blueprint('hashtags',__name__,url_prefix='/hashtags')
api = Api(bp)

hashtag_model = api.parser()
hashtag_model.add_argument('hashtag_name',type=str,required = True)
hashtag_model.add_argument('post_id',type=int,required = True)


@api.route('/hashtag')
class CreateOrGetHashtags(Resource):
    @api.expect(hashtag_model)
    def post(self): # create hashtag
        args = hashtag_model.parse_args()
        hashtag_name = args.get('hashtag_name')
        post_id = args.get('post_id')
        Table().create_hashtag(hashtag_name,post_id)
        return {'status': 1, 'message': 'Хештег успешно добавлен'}

    def get(self,size=20,page=1): # get some hashtags
        all_hashtags = Table.query.all()
        if all_hashtags:
            result = [{'hashtag_id':i.id,'hashtag_name':i.hashtag_name,'post_id':i.post_id,'post':str(i.post)}for i in all_hashtags]
            return {'status': 1, 'message': result}
        return {'status': 0, 'message': 'Хештегов пока нет'}






