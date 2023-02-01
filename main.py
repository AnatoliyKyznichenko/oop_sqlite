from base_queries import DB

db = DB('database.db')
db.create_table('book', 'id INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Link TEXT')

# data = 'test_name','test_link'
# db.insert_data('test', data)

# print(db.select_all('test'))
# print("----------------------------------------")

# db.delete_data('test','Name = "test_name"')

