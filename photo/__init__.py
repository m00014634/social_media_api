from flask import Blueprint
from flask_restx import Resource,Api
from database.models import Photo_post
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename
import os


bp = Blueprint('photo',__name__,url_prefix='/photos')
api = Api(bp)
photo_model = api.parser()
photo_model.add_argument('new_photo',type = FileStorage,location = 'files')

@api.route('/photo')
class GetOrCreatePhotos(Resource):
    def get(self): # get_all_photos
        photos = Photo_post.query.all()
        result = [{i.post_id : i.photo_path} for i in photos]

        return {'status':1,'result':result}

    def create(self): # create_photo
       pass

@api.route('/<int:photo_id>')
class GetChangeDeletePhotoById(Resource):
    def get (self,photo_id): # get_photo_by_id
        current_photo = Photo_post.query.get_or_404(photo_id)

        if current_photo:
            return {'status':1,'photo':{'post_id':current_photo.id,
                                        'photo_locatuion':current_photo.photo_path}}
        return {'status':0,'message':'Нет такой фотографии'}

    @api.expect(photo_model)
    def put (self,photo_id): # change_photo_by_id
        args = photo_model.parse_args()
        new_photo = args.get('new_photo')
        new_photo.save(os.path.join('media/',secure_filename(new_photo.filename)))

        Photo_post().change_post_image(photo_id,new_photo.filename)
        return {'status':1,'message':'Фото успешно изменено'}


    def delete(self,photo_id): # delete_photo_by_id
        Photo_post().delete_post_image(photo_id)

        return {'status':1,'message':'Фотография успешно удалена'}