from . import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))

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