from flask import Blueprint
from flask_restx import Resource,Api,fields
bp = Blueprint('photo',__name__,url_prefix='/photo')
api = Api(bp)

@api.route('/')
class GetOrCreatePhotos(Resource):
    def get(self): # get_all_photos
        pass

    def create(self): # create_photo
       pass

@api.route('/<int:photo_id>')
class GetChangeDeletePhotoById(Resource):
    def get (self,photo_id): # get_photo_by_id
        pass

    def change (self,photo_id): # change_photo_by_id
        pass

    def delete(self,photo_id): # delete_photo_by_id
        pass
