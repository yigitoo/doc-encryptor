#!/bin/python3
'''
@date: May 6, 2023
@author: yigitoo
@brief: This file will used for frontend-backend services of doc-encryptor.
'''
# Libraries i need.
from flask import (
    Flask,
    redirect,
    request,
    jsonify,
    session,
    render_template
)
from db import create_client
import dotenv
import uuid
'''
@brief: Initiliaze components.
'''
app = Flask(__name__, static_folder="gui_static", template_folder='gui_templates')
app.secret_key = str(uuid.uuid4())
users = create_client('users')
config = dotenv.dotenv_values()

'''
@brief: Define this function for getting session_user datas!
'''
def get_session_user() -> dict | None:
    if 'user_id' not in session:
        return None
    user = users.find_one({
        '_id': session['user_id']
    })
    return user

'''
@brief: Routing actions with POST, GET method middlewares.
'''
@app.route('/')
def index():
    session_user = get_session_user()
    if session_user == None:
        return redirect('/login')
    return redirect('/ui')

@app.route('/ui', methods=["POST", "GET"])
def get_encrypted_data():
    session_user = get_session_user()
    if request.method == "GET":
        if session_user is not None:
            return render_template('index.html',user=session_user, project_name="EFELER TOPYATAĞI İÇMESUYU ARITMA 2023")
        
        else:
            return redirect('/')

@app.route('/data', methods=["GET"])
def data():
    encrypted_data = open('f7cada6e025047f39aeb527dc19131184715a971c8ff44d7b27c13f0ebe1a45791f47de7c04445d190af2618d6a209e6840a0f576037433d8fc7d854a9044c841828aa1d633f45ac9e8fc02ddee2251d/out.txt', 'r', encoding='utf-8').read()
    return render_template('data.html', data = encrypted_data)

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect('/')
@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "GET":
        return render_template('login.html', project_name = "Efeler Topyatağı İçmesuyu Arıtma Çalışması Giriş Paneli")
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        user = users.find_one({
            'username': username,
            'password': password
        })
        if user is not None:
            session['user_id'] = user['_id']
            return redirect('/')
if __name__ == "__main__":
    app.run('0.0.0.0', port=4455, debug=1)


"""window = webview.create_window(
    "ÜMİT ŞENYURT | ASKİ ELEKTRONİK TEKNİSYENİ",
    app,
    fullscreen=True
)
webview.start()"""