from flask import Blueprint

bp = Blueprint('posts',__name__,url_prefix='/post')

@bp.get('/')
def get_all_posts():
    pass


@bp.post('/')
def create_post():
    pass


@bp.get('/<int:post_id>')
def get_post_by_id(post_id):
    pass



@bp.put('/<int:post_id>')
def change_post_by_id(post_id):
    pass


@bp.delete('/<int:post_id>')
def delete_post_by_id(post_id):
    pass