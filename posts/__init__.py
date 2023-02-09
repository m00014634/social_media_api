from flask import Blueprint
from flask_restx import Resource,Api,fields
bp = Blueprint('posts',__name__,url_prefix='/post')

# Registration swagger
api = Api (bp)


@api.route('/')
class GetAllPostsOrCreate(Resource):
    def get(self): #Get all posts
        pass

    def post(self): #Create Post
        pass


@api.route('/<int:post_id>')
class GetOrChangeOrDeletePostById(Resource):
    def get(self): # get exact post
        pass

    def change(self): # change exact post
        pass

    def delete(self): # delete exact post
        pass
