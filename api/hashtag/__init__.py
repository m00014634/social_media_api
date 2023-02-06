from flask import Blueprint

bp = Blueprint('hashtags',__name__,url_prefix='/hashtag')


@bp.post('/')
def create_hashtag():
    pass


@bp.get('/')
def get_some_hashtags(size=20,page=1):
    pass


@bp.get('/<string:hashtag_name>')
def get_hashtag_by_name():
    pass




