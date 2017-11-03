import sqlite3
from contextlib import contextmanager


# with
with open('test.csv', 'w') as f_obj:
    f_obj.write('Something')

# open
f_obj = open('test.csv', 'w')
f_obj.write('Nothing')
f_obj.close()


# context manager class
class DataConn:
    """"""

    def __init__(self, db_name):
        """Constructor"""
        self.db_name = db_name

    def __enter__(self):
        """
        Open the database connections
        """
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Close the connection
        """
        self.conn.close()
        if exc_val:
            raise


if __name__ == '__main__':
    db = '/Users/noodle/Desktop/test.db'
    with DataConn(db) as conn:
        cursor = conn.cursor()
