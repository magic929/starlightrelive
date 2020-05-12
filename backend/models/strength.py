from models.config import *
import pandas as pd
from collections import Counter
import math

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


def compute_level():
    percentage = [1/10, 2/10, 3/10, 4/10]
    power = pd.read_sql('SELECT * FROM strength', db.session.bind)
    power = power.set_index('id')
    power = power.values.tolist()
    power = [i for ids in power for i in ids]
    power = Counter(power)
    length = len(power)
    power = power.most_common()
    inds = [math.floor(per * length) for per in percentage]
    result = {
        5: power[0:inds[0]],
        4: power[inds[0]: inds[1]],
        3: power[inds[1]: inds[2]],
        2: power[inds[2]: inds[3]]
    }

    return result