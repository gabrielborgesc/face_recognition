from flask import Flask, request, jsonify, Response
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
import dao
import hashlib
import time
from datetime import datetime
import serivce
from picamera import PiCamera
import face_recognition

app = Flask(__name__) 
cors = CORS(app)


@app.route('/', methods = ['GET'])
def simple():
    return "oi"

@app.route('/signUp', methods = ['POST'])
def signUp():
    name = request.json['name']
    image = take_picture()
    encoded = serivce.npArrayToJson(generate_encoding(image))
    dao.add_user(name, encoded)
    return Response(response="new user successfully registred", status=200)

@app.route('/login', methods = ['POST'])
def login():
    image = take_picture()
    user = serivce.findUser(generate_encoding(image))
    if(user):
        return jsonify({
            "id": user[0],
            "name": user[1]
        })
    return Response(response="user not identified", status=400)



@app.route('/generateNewPassword/<id>', methods = ['POST'])
def generateNewPassword(id):
    user_id = id
    if 'password' in request.json:
        password = request.json['password']
    else:
        password = hashlib.sha256(str(round(time.time())).encode('utf-8')).hexdigest()
    description = request.json['description']
    dao.add_password(user_id, password, description)
    return Response(response="new password successfully registred", status=200)

@app.route('/getUserPasswords/<id>', methods = ['GET'])
@cross_origin()
def getUserPasswords(id):
    result = [{"description": elem[0], "password": elem[1]} for elem in dao.get_user_passwords(id)]
    return jsonify(result)






def take_picture():
    camera = PiCamera()
    camera.capture('tmp/image.jpg')
    camera.close()
    return face_recognition.load_image_file("tmp/image.jpg")

def generate_encoding(picture):
    return face_recognition.face_encodings(picture)[0]


if __name__ == '__main__':
    app.run(host = "0.0.0.0")

