from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

app = Flask(__name__)
api = Api(app)

class Test(Resource):
    def get(self):
        return {
            "response": "success",
            }

    def post(self):
        print(request)
        name = request.json['name']
        email = request.json['email']
        return request.json

    def put(self):
        print('put request: ', request.json)
        name = request.json['name']
        email = request.json['newPassword']
        return {
            "message": "updated"
        }

class TestById(Resource):
    def get(self, id):
        print(request)
        return {
            "response": "success",
            "id": id
            }

        

api.add_resource(Test, '/test')
api.add_resource(TestById, '/testId/<id>')

if __name__ == '__main__':
    app.run()