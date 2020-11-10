from models.config import *
from models import strength

class LevelModel(db.Model):
    __tablename__ = 'Level'

    id = db.Column(db.INTEGER, primary_key=True)
    level = db.Column(db.INTEGER)
    vote = db.Column(db.INTEGER)

def get_level(number):
    return LevelModel.query.filter_by(level=number).all()

def update_level(data):
    for l, chara in data.items():
        for c in chara:
            tmp = LevelModel(id=c[0], level=l, vote=c[1])
            db.session.merge(tmp)
    db.session.commit() 

def get_level_card():
    data = strength.compute_level()
    update_level(data)
    result = {}
    result['ss'] = []
    for record in get_level(5):
        result['ss'].append(record.id)
    result['s'] = []
    for record in get_level(4):
        result['s'].append(record.id)
    result['a'] = []
    for record in get_level(3):
        result['a'].append(record.id)
    result['b'] = []
    for record in get_level(2):
        result['b'].append(record.id)
    return result