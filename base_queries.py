import sqlite3


class DB:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.curs = self.conn.cursor()

    def create_table(self, table_name, columns):
        query = f'CREATE TABLE IF NOT EXISTS {table_name} ({columns})'
        self.curs.execute(query)
        self.conn.commit()

    def select_all(self, table_name):
        query = f'SELECT * FROM {table_name}'
        self.curs.execute(query)
        return self.curs.fetchall()

    def insert_data(self, table_name, data):
        query = f'INSERT INTO {table_name}(Name,Link) VALUES {data}'
        self.curs.execute(query)
        self.conn.commit()

    def delete_data(self, table_name, condition):
        query = f'DELETE FROM {table_name} WHERE {condition}'
        self.curs.execute(query)
        self.conn.commit()

    def update_data(self, table_name, column, value, condition):
        query = f"UPDATE {table_name} SET {column} = '{value}' WHERE {condition}"
        self.curs.execute(query)
        self.conn.commit()

    def search(self, table_name, condition):
        query = f'SELECT * FROM {table_name} WHERE {condition}'
        self.curs.execute(query)
        return self.curs.fetchall()







