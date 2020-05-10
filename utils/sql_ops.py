import sqlite3
import pandas as pd

class Sqlite():
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.c = self.conn.cursor()
    
    def create(self, table, cols, types, primary):
        ct = []
        for c, t in zip(cols, types):
            ct.append("{} {}".format(c, t))
        sqls = 'CREATE TABLE IF NOT EXISTS {} ({}, PRIMARY KEY ({}))'.format(table, ','.join(ct), primary)
        try: 
            self.c.execute(sqls)
        except Exception as e:
            print("error: ", e)
            return 0            
        return 1

    def insert(self, table, data):
        sqls = 'INSERT OR IGNORE INTO ' + table + ' VALUES ({}?)'.format('?,'*(len(data[0]) - 1))
        print(sqls)
        try:
            self.c.executemany(sqls, iter(data))
            self.conn.commit()
        except Exception as e:
            print("error: ", e)
            self.conn.rollback()
    
    def update(self, table, data):
        pass

    def delete(self, table):
        pass
    
    def close(self):
        self.c.close()
        self.conn.close()


class SqlOps():
    def __init__(self):
        self.conn = sqlite3.connect('starlightRe.db')
        self.c = self.conn.cursor()
    
    def create(self, cols, types, primary):
        ct = []
        for c, t in zip(cols, types):
            ct.append("{} {}".format(c, t))
        sqls = 'CREATE TABLE IF NOT EXISTS {} ({}, PRIMARY KEY ({}))'.format(self.table, ','.join(ct), primary)
        try: 
            self.c.execute(sqls)
        except Exception as e:
            print("error: ", e)
            return 0            
        return 1
    
    def insert(self, data):
        sqls = 'INSERT OR IGNORE INTO ' + self.table + ' VALUES ({}?)'.format('?,'*(len(data[0]) - 1))
        print(sqls)
        try:
            self.c.executemany(sqls, iter(data))
            self.conn.commit()
        except Exception as e:
            print("error: ", e)
            self.conn.rollback()
    
    def find_all(self):
        sqls = 'SELECT * FROM {}'.format(self.table)
        results = self.c.execute(sqls)
        return results
    
    def update(self):
        pass
    
    def delete(self):
        pass


class LevelOps(SqlOps):
    def __init__(self):
        super(LevelOps, self).__init__()
        self.table = 'Level'
        self.clos = ''
    
    def find_all(self):
        sqls = 'SELECT * FROM {}'.format(self.table)
        df = pd.read_sql_query(sqls, self.conn)
        return df
    
    def update(self, data):
        sqls = 'REPLACE INTO {} VALUES({}?)'.format(self.table, '?,'*(len(data[0]) - 1))
        print(sqls)
        try:
            self.c.executemany(sqls, iter(data))
            self.conn.commit()
        except Exception as e:
            print("error: ", e)
            self.conn.rollback()


class StrengthOps(SqlOps):
    def __init__(self):
        super(StrengthOps, self).__init__()
        self.table = 'strength'
    
    def find_all(self):
        sqls = 'SELECT * FROM {}'.format(self.table)
        df = pd.read_sql_query(sqls, self.conn)
        return df
