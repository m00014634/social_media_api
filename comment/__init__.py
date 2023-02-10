from flask import Blueprint
from flask_restx import Resource,Api,fields
bp = Blueprint('comments',__name__,url_prefix='/comment')
api = Api(bp)


@api.route('/<int:post_id>')
class CRUDByPostID(Resource):
    def create(self,post_id): # create_comment_to_post_by_post_id
        pass

    def read(self,post_id): # read_comment_by_post_id
         pass

    def update(self,post_id): # update_comment_by_post_id
        pass

    def delete(self,post_id):  # delete_comment_from_post_by_post_id
        pass