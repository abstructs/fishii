from flask import Flask
from flask import request
from flask import jsonify
from flask import g
from flask import send_from_directory
import sys
import os
import sqlite3 

static_file_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'public')

DATABASE = 'fishbase.db'

app = Flask(__name__)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

@app.route("/")
def index():
    db = get_db()
    query_db("SELECT * FROM User")
    return jsonify(request.args)

@app.route("/signup")
def signup():
    username = request.args.get('username')
    password = request.args.get('password')

    return query_db("SELECT username FROM User WHERE username=?", username)

    verify_user(username, password) 

    if verify_user(username, password):
        return "Success"
    else:
        return "failure"
    db = get_db()
    query_db("SELECT username FROM User")
    return jsonify()

def verify_user(username, password):
    try:
        if not(len(username) > 0 and len(username) < 16):
            print("\n\n\n", file=sys.stderr)
            
    except TypeError:
        return False