from main import db
from werkzeug.security import generate_password_hash,check_password_hash

# User's table

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True,autoincrement = True)
    username = db.Column(db.String,nullable = False)
    first_name =  db.Column(db.String,nullable = False)
    last_name = db.Column(db.String,nullable = True)
    email = db.Column(db.String, nullable=False)
    phone_number =  db.Column(db.String,nullable = False,unique =True)
    about =  db.Column(db.String,nullable = True)

    # Create user
    def registration(self,username,first_name,last_name,email,phone_number,about):
        new_user = User(username=username, first_name=first_name, last_name=last_name, email=email,
                        phone_number=phone_number, about=about)

        db.session.add(new_user)
        db.session.commit()


    # Change username
    def change_username(self,user_id,new_username):
        user = User.query.get_or_404(user_id)
        # validating
        if user.username == new_username:
            return 'Новое имя должно отличаться от старого'

        user.username = new_username
        db.session.commit()



    # change phone number
    def change_phone_number(self, user_id, new_phone_number):
        user = User.query.get_or_404(user_id)
        if user.email == new_phone_number:
            return 'Новый номер должен отличаться от старого'
        user.email = new_phone_number
        db.session.commit()


    # change email
    def change_email(self,user_id,new_email):
        user = User.query.get_or_404(user_id)
        if user.email == new_email:
            return 'Новый email должен отличаться от старого'
        user.email  = new_email
        db.session.commit()


     # change "about"
    def change_about(self,user_id,new_about):
        user = User.query.get_or_404(user_id)
        user.email  = new_about
        db.session.commit()



# Post table
class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    header = db.Column(db.String,nullable = False)
    main_text = db.Column(db.String,nullable = False)
    publish_date = db.Column(db.DateTime)
    user_id = db.Column(db.Integer,db.ForeignKey ('users.id'))
    post_likes = db.Column(db.Integer, default=0)
    user = db.relationship('User')

    # change main_text
    def change_main_text(self,post_id,new_main_text):
        current_post = Post.query.get_or_404(post_id)

        if current_post == new_main_text:
            return 'В новом тексте нет никаких изменений'

        current_post.main_text = new_main_text
        db.session.commit()


    # Change header
    def change_header(self,post_id,new_header):
        current_post = Post.query.get_or_404(post_id)

        if current_post == new_header:
            return 'В новом заголовке нет никаких изменений'

        current_post.header = new_header
        db.session.commit()


    # Delete post
    def delete_post(self,post_id):
        current_post = Post.query.get_or_404(post_id)
        db.session.delete(current_post)
        db.session.commit()



# Photo table
class Photo_post(db.Model):
    __tablename__ = 'photos_for_post'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    photo_path = db.Column(db.String,nullable = False)
    post_id = db.Column(db.Integer,db.ForeignKey('posts.id',ondelete = 'SET NULL'))
    post = db.relationship('Post')



# Comments table
class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String,nullable = False)
    likes = db.Column(db.Integer,nullable = True,default = 0)
    data = db.Column(db.DateTime)

    post_id = db.Column(db.Integer,db.ForeignKey('posts.id',ondelete = 'SET NULL'))

    # delete comment
    def delete_comment(self,comment_id):
        current_comment = Comment.query.get_or_404(comment_id)
        db.session.delete(current_comment)
        db.session.commit()

    # Likes
    def likes_detect(self,comment_id):
        current_comment = Comment.query.get_or_404(comment_id)
        current_comment.likes += 1
        db.session.commit()




    # Change comment text
    def change_comment_text(self,comment_id,new_comment_text):
        current_comment = Comment.query.get_or_404(comment_id)
        if current_comment ==new_comment_text:
            return 'Ничего не изменено в комментариях'

        current_comment.text = new_comment_text
        db.session.commit()


# Hashtag table
class Table(db.Model):
    __tablename__ = 'hashtags'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    hashtag_name = db.Column(db.String,nullable = False, unique = True)
    post_id = db.Column(db.Integer,db.ForeignKey('posts.id',ondelete = 'SET NULL'))
    post = db.relationship('Post')



# Password table
class Passwords(db.Model):
    __tablename__ = 'passwords'
    password = db.Column(db.String,nullable = False)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id',ondelete = 'SET NULL'),primary_key = True)
    users = db.relationship('User')

    # Password generate
    def set_password(self,password):
        self.password = generate_password_hash(password)

    # Check password
    def check_password(self,password):
        return check_password_hash(self.password,password)


    ## hw ##
    # Change password
    def change_password(self,user_id,new_password):
        current_password = Passwords.query.get_or_404(user_id)

        if current_password == new_password:
            return 'В пароле ничего не изменено'
        current_password.password = new_password
        db.session.commit()

