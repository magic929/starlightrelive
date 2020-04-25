import sys
from utils.sql_ops import Sqlite
from utils import utils

field = ["chara1","chara2", "chara3", "chara4", "chara5"]

types = ["TEXT", "TEXT", "TEXT", "TEXT", "TEXT"]

def insert_strength(data):
    strength = Sqlite("starlightRe.db")
    strength.create("strength", field, types, primary)
    strength.insert("strength", data)
    strength.close()


def create_strength():
    strength = Sqlite("starlightRe.db")
    ct = []
    for c, t in zip(field, types):
        ct.append("{} {}".format(c, t))
    sql = 'CREATE TABLE IF NOT EXISTS {} (id INTEGER PRIMARY KEY NOT NULL, {})'.format("strength", ','.join(ct))
    print(sql)
    try:
        strength.c.execute(sql)
    except Exception as e:
        print("error: ", e)
        return 0
    strength.close()


if __name__ == "__main__":
    # data = utils.read_image(sys.argv[1])
    # data = read_file(sys.argv[1])
    create_strength()