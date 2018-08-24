from app import db, ma
from common import utils


class Locations(db.Model):
    __tablename__ = 'locations'

    location_id = db.Column(db.String(45), primary_key=True)
    name = db.Column(db.String(45))
    type = db.Column(db.String(45))
    level = db.Column(db.Integer)
    status = db.Column(db.String(45))


class LocationsSchema(ma.Schema):
    class Meta(object):
        fields = utils.class_attributes(Locations)


LOCATION_SCHEMA = LocationsSchema()
LOCATIONS_SCHEMA = LocationsSchema(many=True)
