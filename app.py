from flask import Flask, jsonify, redirect, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


# db = sa.create_engine("mysql+pymysql://root:root@localhost:3306/local_test")

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI']= 'mysql+pymysql://root:root@localhost:3306/local_test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

DB = db.Model
MA = ma.Schema


class MainHandler(Resource):
    def get(self):

        return {'msg': 'Hello World!'}

    def post(self):
        pass

from model.rules_meta import RuleMeta, RULEMETA_SCHEMA, RULESMETA_SCHEMA
# from model.rules import Rules, RULE_SCHEMA, RULES_SCHEMA
class RulesHandler(Resource):
    def get(self):
        qry = RuleMeta.query.get(4)

        return RULEMETA_SCHEMA.jsonify(qry)


from model.components import Components, COMPONENT_SCHEMA, COMPONENTS_SCHEMA
class ComponentsHandler(Resource):
    def get(self):
        qry = Components.query.get('Charger')

        return COMPONENT_SCHEMA.jsonify(qry)

from model.categories import Categories, CATEGORY_SCHEMA, CATEGORIES_SCHEMA
class CategoriesHandler(Resource):
    def get(self):
        qry = Categories.query.all()

        return COMPONENTS_SCHEMA.jsonify(qry)


class Create(Resource):
    def get(self):
        return {'msg': 'from here you can create rules'}

api.add_resource(MainHandler, '/')
api.add_resource(RulesHandler, '/rules')
api.add_resource(Create, '/rules/create')
api.add_resource(ComponentsHandler, '/components')
api.add_resource(CategoriesHandler, '/categories')


if __name__ == '__main__':
    app.run(port=5001)
