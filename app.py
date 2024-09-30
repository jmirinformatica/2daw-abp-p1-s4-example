from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

# Llegeixo la configuració del config.py de l'arrel
app.config.from_object('config.Config')

@app.route('/')
def init():
    return redirect(url_for('items_list'))

@app.route('/items/list')
def items_list():
    return render_template('items_list.html')
