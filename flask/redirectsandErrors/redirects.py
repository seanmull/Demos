from flask import abort, redirect, url_for, Flask, render_template

app = Flask(__name__)

@app.route('/'   )
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    abort(404)
    # this_is_never_executed()
