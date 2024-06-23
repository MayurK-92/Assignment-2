from flask import Flask, render_template, redirect, url_for, request, session
from config import Config
from models import init_app, register_user, validate_user

app = Flask(__name__)
app.config.from_object(Config)
init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    register_user(username, password)
    return redirect(url_for('index'))

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if validate_user(username, password):
        session['username'] = username
        return redirect(url_for('home'))
    else:
        return 'Invalid Credentials', 401

@app.route('/home')
def home():
    if 'username' in session:
        return f'Hello, {session["username"]}!'
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
