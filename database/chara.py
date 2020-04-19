import sys

from utils.sql_ops import Sqlite
from utils import utils

field = ["id", "name", "name_ruby", "department_1", "department_2",
         "likes", "dislikes", "like_foods", "dislike_foods", "introduction"]

types = ["INTEGER", "TEXT", "TEXT", "TEXT", "TEXT",
         "TEXT", "TEXT", "TEXT", "TEXT", "TEXT"]

primary = "id"

def insert_chara(data):
    chara = Sqlite("starlightRe.db")
    chara.create("chara", field, types, primary)
    chara.insert("chara", data)
    chara.close()

if __name__ == "__main__":
    data = utils.read_file(sys.argv[1], field)
    print(data[0])
    insert_chara(data)