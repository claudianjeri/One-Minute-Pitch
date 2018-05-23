class Pitch:
    all_pitches = []

    def __init__(self,category,pitch)::
       
        self.category = category
        self.pitch = pitch
       
    def save_pitch(self):
        Pitch.all_pitches.append(self)


    @classmethod
    def delete_pitch(cls):
        Pitch.all_pitches.clear()