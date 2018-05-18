from flask import Flask, jsonify, redirect, request
from flask_restful import Resource, Api
import sqlalchemy as sa


app = Flask(__name__)
api = Api(app)


class Home(Resource):
    def get(self):
        return {'msg': 'Hello World!'}

    def post(self):
        pass


api.add_resource(Home, '/')

if __name__ == '__main__':
    app.run()
