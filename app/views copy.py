# from flask import render_template, url_for, redirect, g, abort, request
# from app import app
# from app.forms import TaskForm
# import json
# from flask import jsonify

# # rethink imports
# import rethinkdb as r
# from rethinkdb.errors import RqlRuntimeError
# from rethinkdb.errors import RqlDriverError

# # rethink config
# RDB_HOST = 'localhost'
# RDB_PORT = 28015
# TODO_DB = 'todo'
# rdb = r.RethinkDB()
# connection = rdb.connect(host = RDB_HOST, port = RDB_PORT)

# #db setup; only run once
# def dbsetup():
#     connection = rdb.connect(host = RDB_HOST, port = RDB_PORT)
#     try:
#         rdb.db_create(TODO_DB).run(connection)
#         rdb.db(TODO_DB).table_create("todos").run(connection)
#         print("Database setup connection")
#     except RqlRuntimeError:
#         print('Database already exists')
#     finally:
#         connection.close()
# dbsetup()

# #open connection before each request
# @app.before_request #This is a decorator provided by Flask.#It indicates that the 
# # #following function (before_request()) should be executed before each request to 
# # #any route in the Flask application.
# def before_request():
#     try:
#         g.rdb_conn = rdb.connect(host = RDB_HOST, port = RDB_PORT, db = TODO_DB)
#     except RqlDriverError:
#         abort(503, "Database connection could be established")

# #close connection after each request
# @app.after_request
# def after_request(exception):
#     try:
#         g.rdb_conn.close()
#         #In summary, the g object in Flask serves as a request-local storage mechanism, 
#         # allowing you to store and access data that is relevant to the current 
#         # request context throughout the request handling process. It provides a convenient and thread-safe way 
#         # to share data within the scope of a single request without affecting other requests.
#     except AttributeError:
#         pass
# todos = []
# @app.route('/', methods = ['POST'])
# def index():

#     # form = TaskForm()
#     # # selection = list(rdb.table('todos').run(g.rdb_conn))
#     # selection = list(g.rdb_conn.run(rdb.table('todos')))
#     # print(selection)
#     # return render_template('index.html', form=form, task=selection)
#     todos.append(jsonify(request.json))
#     print(todos)
#     return request.json

# @app.route("/",  methods = ['GET'])
# def index2():
#     # form = TaskForm()
#     # # selection = list(rdb.table('todos').run(g.rdb_conn))
#     # selection = list(g.rdb_conn.run(rdb.table('todos')))
#     # print(selection)
#     # return render_template('index.html', form=form, task=selection)
#     return jsonify({"todos":todos})
