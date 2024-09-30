from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)
app.config["SECRET_KEY"] = "Valor aleatori molt llarg i super secret"

@app.route('/')
def init():
    return redirect(url_for('items_list'))

@app.route('/items/list')
def items_list():
    return render_template('items_list.html')
