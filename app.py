from flask import Flask, redirect, url_for, render_template, request
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
    return redirect(url_for('items_list'))

@app.route('/items/list')
def items_list():
    with get_db_connection() as con:
        res = con.execute("SELECT id, nom, unitats FROM items ORDER BY id ASC")
        items = res.fetchall()

    return render_template('items_list.html', items = items)

@app.route('/items/update/<int:item_id>', methods = ['POST', 'GET'])
def items_update(item_id):
    if request.method == 'GET':
        with get_db_connection() as con:
            res = con.execute("SELECT id, nom, unitats FROM items WHERE id = ?", (item_id, ))
            item = res.fetchone()

        return render_template('items_update.html', item = item)

    else: # POST
        nom = request.form['nom']
        unitats = int(request.form['unitats']) # es text, el passo a enter

        with get_db_connection() as con:
            con.execute(
                "UPDATE items SET nom = ?, unitats = ? WHERE id = ?", 
                (nom, unitats, item_id)
            )

        # https://en.wikipedia.org/wiki/Post/Redirect/Get
        return redirect(url_for('items_update', item_id = item_id))
