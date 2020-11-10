from utils.sql_ops import LevelOps

fields = ['id', 'level', 'vote']
types = ['INTEGER', 'INTEGER', 'INTEGER']
primary = 'id'


if __name__ == '__main__':
    level = LevelOps()
    level.create(fields, types, primary)