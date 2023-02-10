from flask import Blueprint
from flask_restx import Resource,Api,fields

bp = Blueprint('hashtags',__name__,url_prefix='/hashtag')
api = Api(bp)

@api.route('/')
class CreateOrGetHashtags(Resource):
    def create(self): # create hashtag
        pass

    def get(self,size=20,page=1): # get some hashtags
        pass


@api.route('/<string:hashtag_name>')
class GetHashtagByName(Resource):
    def get(self,hashtag_name): # get hashtag by name
        pass




