class Pitch:
    all_pitches = []

    def __init__(self,category,pitch):
       
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