#!/bin/python3
'''
@date: May 6, 2023
@author: yigitoo
@brief: This file will used for backend services of doc-encryptor.
'''
# Libraries i need.
from flask import (
    Flask,
    redirect,
    request,
    send_file,
    jsonify
)
from db import create_client

'''
@brief: initliaze components.
'''
app = Flask(__name__, static_folder="encrypted_data")
users = create_client('users')

'''
@brief: Routing actions with POST, GET method middlewares.
'''
@app.route('/')
def index():
    return jsonify({
        "status": 404,
        "message": "This page is not found in server."
    })

@app.route('/get_data', methods=["POST", "GET"])
def get_encrypted_data():
    if request.method == "GET":
        return redirect('/')
    
    if request.method == "POST":
        file = open('encrypted_data/enc_data.dat', 'r')
        
        enc_data = file.read()
        
        file.close()

        data = request.json
        username = data['username']
        password = data['password']

        user = users.find_one({
            "username": username,
            "password": password
        })

        if user is not None:
            return enc_data
        else:
            return redirect('/')
if __name__ == "__main__":
    app.run('0.0.0.0', port=4455, debug=1)
