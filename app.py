from flask import Flask, redirect, url_for, render_template
import sqlite3
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = "Valor aleatori molt llarg i super secret"


# ruta absoluta d'aquesta carpeta
basedir = os.path.abspath(os.path.dirname(__file__)) 

def get_db_connection():
    sqlite3_database_path =  basedir + "/database.db"
    con = sqlite3.connect(sqlite3_database_path)
    # https://docs.python.org/3/library/sqlite3.html#how-to-create-and-use-row-factories
    con.row_factory = sqlite3.Row
    return con

@app.route('/')
def init():
    return redirect(url_for('item_list'))

@app.route('/item')
def item_list():
    with get_db_connection() as con:
        res = con.execute("SELECT id, nom, unitats FROM items ORDER BY id ASC")
        items = res.fetchall()

    return render_template('item_list.html', items = items)

