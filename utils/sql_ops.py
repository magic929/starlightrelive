import sqlite3

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
