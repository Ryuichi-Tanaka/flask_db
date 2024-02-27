import sqlite3
from flask import g

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect('memo.db')
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(exception=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
    
def init_db():
    con = sqlite3.connect('memo.db')
    con.execute("DROP TABLE IF EXISTS POST")
    con.execute("CREATE TABLE POST (\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        USER TEXT, \
        URINE TEXT, \
        breastfeeding TEXT, \
        FLIGHT TEXT, \
        DATE TEXT DEFAULT (DATE('now')))")
    print('データベースを初期化しました')


if __name__ == '__main__':
    init_db()