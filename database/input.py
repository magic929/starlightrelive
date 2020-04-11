import ast
import re
import sys

from utils.sql_ops import Sqlite


field = ["id", "name", "chara_id", "cost", "base_agi", "base_rarity", "growth_board3_id", "base_pdef", "delta_agi", 
        "dex", "growth_board7_id", "eva", "growth_board1_id", "party_skill_type", "delta_pdef", 
        "growth_board6_id", "attribute_id", "growth_board4_id", "dress_episode_id", "base_atk", 
        "delta_atk", "auto_skill2_id", "party_skill_id", "auto_skill2_type", "delta_hp", "auto_skill1_id",
        "command_skill1_id", "auto_skill1_type", "attack_type", "growth_board5_id", "command_skill2_id",
        "auto_skill3_type", "delta_mdef", "auto_skill3_id", "cri", "growth_board8_id", "hit", "base_mdef",
        "growth_board2_id", "growth_board9_id", "command_skill3_id", "published_at", "command_unique_skill_id",
        "dress_type", "base_hp", "description"]

types = ["TEXT", "TEXT", "INTEGER", "INTEGER", "INTEGER", "INTEGER", "TEXT", "INTEGER", "INTEGER",
        "INTEGER", "TEXT", "INTEGER", "TEXT", "INTEGER", "INTEGER",
        "TEXT", "INTEGER", "TEXT", "TEXT", "INTEGER",
        "INTEGER", "TEXT", "TEXT", "INTEGER", "INTEGER", "TEXT",
        "TEXT", "INTEGER", "INTEGER", "TEXT", "TEXT",
        "INTEGER", "INTEGER", "TEXT", "INTEGER", "TEXT", "INTEGER", "INTEGER",
        "TEXT", "TEXT", "TEXT", "TIMESTAMP", "TEXT",
        "INTEGER", "INTEGER", "TEXT"]

primary = 'ID'

def append_suffix(matched):
    tempstr = matched.group()
    tempstr = tempstr[0] + "\"" + tempstr[1:] + "\""
    return tempstr

def read_file(path):
    with open(path, "r", encoding='utf8') as f:
        data = f.read()
    
    data = data.replace("return", "").replace("=", ":").replace("[[", "\"").replace("]]", "\"")
    data = re.sub(r"[\[\]\. ]", "", data)
    data = re.sub(r"(\t|:)[a-zA-z0-9_]+", append_suffix, data)
    data = re.sub(r"\s+", "", data)
    with open("test.txt", "w", encoding="utf8") as f:
        f.write(data)
    data = ast.literal_eval(data)
    result = []
    for key, value in data.items():
        tmp = [key]
        for f in field[1:]:
            if isinstance(value[f], dict):
                tmp.append(value[f]['ja'])
            else:
                tmp.append(value[f])
        
        result.append(tuple(tmp))
    
    return result


def insert_dress(data):
    dress = Sqlite("starlightRe.db")
    dress.create("dress", field, types, primary)
    dress.insert("dress", data)
    dress.close()


if __name__ == "__main__":
    data = read_file(sys.argv[1])
    insert_dress(data)