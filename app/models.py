from . import db, login_manager
from werkzeug.security import generate_password_hash,check_password_hash #generate takes in a password and return  hash and check does the opposite.
from flask_login import UserMixin

@login_manager.user_loaderdef load_user(user_id):
return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255), index= True)
    password_hash = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index = True)
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)
    
    def __repr__(self):
        return f'User {self.username}'


        
class Pitch:
    all_pitches = []

    def __init__(self,name,category,pitch):
        self.name = name
        self.category = category
        self.pitch = pitch
       
    def save_pitch(self):
        Pitch.all_pitches.append(self)


    @classmethod
    def delete_pitch(cls):
        Pitch.all_pitches.clear()

    @classmethod
    def get_pitches(cls, usname):
        repsonse = []

        for pitch in cls.all_pitches:
            response.append(pitch)
        return response