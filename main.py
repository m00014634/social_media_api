from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database connection
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///media.db'
app.config['UPLOAD_FOLDER'] = 'media' # Indicate path to media
db.init_app(app)

from comment import bp as comment_bp
from hashtag import bp as hashtag_bp
from user import bp as user_bp
from posts import bp as posts_bp
from photo import bp as photo_bp
from authentification import bp as auth_bp

# Component registration


app.register_blueprint(comment_bp)
app.register_blueprint(hashtag_bp)
app.register_blueprint(user_bp)
app.register_blueprint(posts_bp)
app.register_blueprint(photo_bp)
app.register_blueprint(auth_bp)
@app.route('/hello')
def hellower():
    return 'Hello world'



if __name__ == '__main__':
    app.run()