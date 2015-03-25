import web

table_name = 'todo'
db_name = 'guest'
db = web.database(dbn= 'mysql', db = db_name, user = 'guest', pw = 'guest')

def get_todos():
	return db.select(table_name, order='id')

def new_todo(text):
	db.insert(table_name, title=text)

def del_todo(id):
	db.delete(table_name, where="id=$id", vars=locals())
