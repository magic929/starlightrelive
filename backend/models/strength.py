from models.config import *

class StrengthModel(db.Model):
    __tablename__ = 'strength'

    id = db.Column(db.INTEGER, primary_key=True)
    chara1 = db.Column(db.TEXT)
    chara2 = db.Column(db.TEXT)
    chara3 = db.Column(db.TEXT)
    chara4 = db.Column(db.TEXT)
    chara5 = db.Column(db.TEXT)

def insert_one(values):
    data = StrengthModel(chara1=values[0], chara2=values[1], chara3=values[2], chara4=values[3], chara5=values[4])
    db.session.add(data)
    db.session.commit()