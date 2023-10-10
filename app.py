from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)
app.config["SECRET_KEY"] = "Valor aleatori molt llarg i super secret"

@app.route('/')
def init():
    return redirect(url_for('item_list'))

@app.route('/item')
def item_list():
    return render_template('item_list.html')
