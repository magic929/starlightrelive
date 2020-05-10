from utils.sql_ops import StrengthOps, LevelOps
from collections import Counter
import math

strength = StrengthOps()
level = LevelOps()
percentage = [1/10, 2/10, 3/10, 4/10]

def compute_level():
    power = strength.find_all()
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


def insert_level(data):
    inserted = []
    for l, chara in data.items():
        for c in chara:
            tmp = (c[0], c[1], l)
            inserted.append(tmp)
    
    # print(type(level))
    level.update(inserted)


if __name__ == "__main__":
    data = compute_level()
    insert_level(data)  
