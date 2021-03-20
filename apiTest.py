from flask import Flask, request, jsonify, Response
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
import dao
import hashlib
import time
from datetime import datetime
import numpy as np
from encodingsGenerator import EncodingsGenerator
import cv2
import serivce

encoder = EncodingsGenerator()

app = Flask(__name__) 

@app.route('/signUp', methods = ['POST'])
def signUp():
    name = request.json['name']
    img = cv2.imread("files/images/"+name+".jpeg") # it will be replaced by img from camera
    encoded = serivce.npArrayToJson(encoder.generateEncoding(img))
    dao.add_user(name, encoded)
    return Response(response="new user successfully registred", status=200)

@app.route('/login', methods = ['POST'])
def login():
    name = request.json['name'] # it not will be necesssary. User click on login e we simply get your face
    img = cv2.imread("files/images/"+name+".jpeg") # it will be replaced by img from camera
    encodings = encoder.generateEncoding(img)
    user = serivce.findUser(encodings)
    if(user):
        return {
            "id": user[0],
            "name": user[1]
        }
    return Response(response="user not identified", status=400)


@app.route('/generateNewPassword/<id>', methods = ['POST'])
def generateNewPassword(id):
    user_id = id
    password = hashlib.sha256(str(round(time.time())).encode('utf-8')).hexdigest()
    description = request.json['description']
    dao.add_password(user_id, password, description)
    return Response(response="new password successfully registred", status=200)

@app.route('/getUserPasswords/<id>', methods = ['GET'])
def getUserPasswords(id):
    result = dao.get_user_passwords(id)
    return jsonify(result)


if __name__ == '__main__':
    app.run()