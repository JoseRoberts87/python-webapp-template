from flask import Flask, jsonify, redirect, request
from flask_restful import Resource, Api
import sqlalchemy as sa

db = sa.create_engine("mysql+pymysql://root:root@localhost:3306/local_test")

app = Flask(__name__)
api = Api(app)

class Home(Resource):
    def get(self):
        data = db.execute("SELECT * FROM data;")
        return {'msg': 'Hello World! %s' % (data.fetchall())}

    def post(self):
        pass


class Rules(Resource):
    def get(self):
        return {'msg': 'list of rules'}


class GetRule(Resource):
    def get(self):
        return {'msg': 'returning rule'}


class Create(Resource):
    def get(self):
        return {'msg': 'from here you can create rules'}


api.add_resource(Home, '/')
api.add_resource(Rules, '/rules')
api.add_resource(Create, '/rules/create')
api.add_resource(GetRule, '/rule/{id}')

if __name__ == '__main__':
    app.run()
