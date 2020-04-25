import sys
from utils.sql_ops import Sqlite
from utils import utils

field = ["id","img_url"]

types = ["TEXT", "TEXT"]

primary = 'ID'

def insert_img(data):
    chara = Sqlite("starlightRe.db")
    chara.create("img", field, types, primary)
    chara.insert("img", data)
    chara.close()


if __name__ == "__main__":
    data = utils.read_image(sys.argv[1])
    # data = read_file(sys.argv[1])
    insert_img(data)