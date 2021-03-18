from flask import Flask, request, jsonify, Response
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
import dao

app = Flask(__name__)
api = Api(app)

class Users(Resource):

    def get(self):
        return jsonify(dao.get_all_users())

    

class User(Resource):
    def get(self):
        name = request.args.get("name")
        result = dao.get_user(name)
        return jsonify(result)

    def post(self):
        name = request.json['name']
        encoded = [1, 2.5, 6.7, -2, -3.4] #it will be get from code with cv2, dlib, etc
        dao.add_user(name, encoded)
        status_code = Response(response="new user successfully added", status=200)
        return status_code

api.add_resource(Users, '/users')
api.add_resource(User, '/user')

if __name__ == '__main__':
    app.run()