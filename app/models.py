from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):
    __tablename__= 'users'
    id=db.Column(db.Integer,primary_key =True)
    username = db.Column(db.String(255))
    email=db.Column(db.String(255),unique=True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_hash =db.Column(db.String(255))
    pitches= db.relationship('Pitch',backref='user',lazy="dynamic")


    @property
    def password(self):
        raise AttributeError('You cannnot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_hash = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_hash,password)

    def save_user(self):
        db.session.add(self)
        db.session.commit()

        
    def __repr__(self):
        return f'User {self.username}'

class Pitch(db.Model):
    __tablename__='pitch'
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(255))
    description=db.Column(db.String)
    upvote = db.Column(db.Integer)
    downvote = db.Column(db.Integer)
    comments_id = db.relationship('Comments',backref = 'iscomment', lazy = 'dynamic')
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))


    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls):
        '''
        gets pitches from the database
        '''
        pitch =Pitch.query.all()
        return pitch


    
class Comments(db.Model):
    __tablename__ ='comments'
   
    id = db.Column(db.Integer,primary_key = True)
    pitch_id = db.Column(db.Integer,db.ForeignKey("pitch.id"))
    comment = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

#     def __repr__(self):
#         return f"Comment('{self.comment}', '{self.posted}')"

       
#     @classmethod
#     def get_comments(cls):
#         '''
#         Function that queries the Groups Table in the database and returns all the information from the Groups Table
#         Returns:
#             groups : all the information in the groups table
#         '''

#         comments = Comments.query.all()

#         return comments