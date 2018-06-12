from flask import Flask, jsonify, redirect, request, make_response
from flask_restful import Resource, Api, output_json, reqparse
from flask_restful.representations import json
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


# db = sa.create_engine("mysql+pymysql://root:root@localhost:3306/local_test")

app = Flask(__name__)
api = Api(app, catch_all_404s=True)
app.config['SQLALCHEMY_DATABASE_URI']= 'mysql+pymysql://root:root@localhost:3306/local_test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

# DB = db.Model
# MA = ma.Schema

parser = reqparse.RequestParser()

d_type_header = {'ContentType':'application/json'}
from common import utils

class MainHandler(Resource):
    def get(self):

        return output_json({'msg': 'Hello World!'},200, d_type_header)

    def post(self):
        pass

from model.rules_meta import RuleMeta, RULEMETA_SCHEMA, RULESMETA_SCHEMA
# from model.rules import Rules, RULE_SCHEMA, RULES_SCHEMA
class RulesMetaHandler(Resource):
    def get(self):
        qry = RuleMeta.query.all()
        data = RULESMETA_SCHEMA.dump(qry)
        status = utils.check_status(data)

        return output_json(data, status, d_type_header)
        # return RULESMETA_SCHEMA.jsonify(qry)

from model.components import Components, COMPONENT_SCHEMA, COMPONENTS_SCHEMA
class ComponentsHandler(Resource):
    def get(self):
        qry = Components.query.all()
        data = COMPONENTS_SCHEMA.dump(qry)
        status = utils.check_status(data)

        return output_json(data, status, d_type_header)

from model.categories import Categories, CATEGORY_SCHEMA, CATEGORIES_SCHEMA
class CategoriesHandler(Resource):
    def get(self):
        qry = Categories.query.all()
        data = CATEGORIES_SCHEMA.dump(qry)
        status = utils.check_status(data)

        return output_json(data, status, d_type_header)

from model.locations import Locations, LOCATION_SCHEMA, LOCATIONS_SCHEMA
class LocationsHandler(Resource):
    def get(self):
        qry = Locations.query.all()
        data = LOCATIONS_SCHEMA.dump(qry)
        status = utils.check_status(data)

        return output_json(data, status, d_type_header)

    def post(self):
        obj = ''
        utils.write_to_db(obj)

from model.part_numbers import PartNumbers, PARTNUMBER_SCHEMA, PARTNUMBERS_SCHEMA
class PartNumbersHandler(Resource):

    def get(self):
        qry = PartNumbers.query.all()
        data = PARTNUMBERS_SCHEMA.dump(qry)
        status = utils.check_status(data)

        return output_json(data, status, d_type_header)

    def post(self):
        json_data = request.get_json(force=True)
        # check if json is empty
        # check if json is complete
        # check if json object found in database
        # if not empty, is complete and not found, persist

        # data = utils.find(PartNumbers, {'part_number_id': 'part1'})

        data = utils.val_request(model=PartNumbers, json_data=json_data,
                               att={'part_number_id': json_data['part_number_id']})
        if data[1] == 200:
            print('everythings ok :' , data)
            # print(**json_data)

            utils.write_to_db(PartNumbers, json_data)

        return output_json(data[0], data[1], d_type_header)

class Create(Resource):
    def get(self):
        return {'msg': 'from here you can create rules'}



api.add_resource(MainHandler, '/')
api.add_resource(RulesMetaHandler, '/rules-meta')
api.add_resource(ComponentsHandler, '/components')
api.add_resource(CategoriesHandler, '/categories')
api.add_resource(LocationsHandler, '/locations')
api.add_resource(PartNumbersHandler, '/part-numbers')

api.add_resource(Create, '/rules/create')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
