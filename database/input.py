import sys

from utils.sql_ops import Sqlite
from utils import utils


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
        "TEXT", "TEXT", "TEXT", "TEXT", "TEXT",
        "INTEGER", "INTEGER", "TEXT"]

primary = 'ID'


def insert_dress(data):
    dress = Sqlite("starlightRe.db")
    dress.create("dress", field, types, primary)
    dress.insert("dress", data)
    dress.close()


if __name__ == "__main__":
    data = utils.read_file(sys.argv[1], field)
    # data = read_file(sys.argv[1])
    insert_dress(data)