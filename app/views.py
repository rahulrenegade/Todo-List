from flask import render_template, url_for, redirect, g, abort, request
from app_testing import app
from app_testing.forms import TaskForm

# rethink imports
import rethinkdb as r
from rethinkdb.errors import RqlRuntimeError
from rethinkdb.errors import RqlDriverError

# rethink config
RDB_HOST = 'localhost'
RDB_PORT = 28015
TODO_DB = 'todo'
rdb = r.RethinkDB()


#db setup; only run once
def dbsetup():
    connection = rdb.connect(host = RDB_HOST, port = RDB_PORT)
    try:
        rdb.db_create(TODO_DB).run(connection)
        rdb.db(TODO_DB).table_create("todos").run(connection)
        print("Database setup connection")
    except RqlRuntimeError:
        print('Database already exists')
    finally:
        connection.close()
dbsetup()

#open connection before each request
@app.before_request 
def before_request():
    try:
        g.rdb_conn = rdb.connect(host = RDB_HOST, port = RDB_PORT, db = TODO_DB)
    except RqlDriverError:
        abort(503, "Database connection could be established")

#close connection after each request
@app.teardown_request
def after_request(exception):
    try:
        g.rdb_conn.close()
    except AttributeError:
        pass

@app.route("/", methods = ['POST', 'GET'])
def index():
    form = TaskForm()
    if form.validate_on_submit():
        rdb.table('todos').insert({'name':form.label.data}).run(g.rdb_conn)
        return redirect(url_for('index'))
    selection = list(rdb.table('todos').run(g.rdb_conn))
    return render_template('index.html', form=form, tasks=selection)

@app.route("/delete/<string:id>")
def delete_task(id):
    try:
        rdb.table("todos").filter({"id": id}).delete().run(g.rdb_conn)
        return redirect(url_for('index'))    
    except:
        print('there was a problem in the deleting the task')
