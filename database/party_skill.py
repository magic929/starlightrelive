import sys
from utils.sql_ops import Sqlite
from utils import utils

field = ["description","skill_option1_values", "skill_option2_values", "skill_option3_values", "skill_option4_values", "skill_option5_values"]

types = ["TEXT", "TEXT", "TEXT", "TEXT", "TEXT", "TEXT"]

def insert_party(data):
    party = Sqlite("starlightRe.db")
    party.insert_auto("party", data)
    party.close()


def create_party():
    party = Sqlite("starlightRe.db")
    ct = []
    for c, t in zip(field, types):
        ct.append("{} {}".format(c, t))
    sql = 'CREATE TABLE IF NOT EXISTS {} (id INTEGER PRIMARY KEY NOT NULL, {})'.format("party", ','.join(ct))
    print(sql)
    try:
        party.c.execute(sql)
    except Exception as e:
        print("error: ", e)
        return 0
    party.close()


if __name__ == "__main__":
    # data = utils.read_image(sys.argv[1])
    data = utils.read_fix(sys.argv[1], field)
    # create_party()
    insert_party(data)