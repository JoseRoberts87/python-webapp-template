from app import db, ma
from common import utils

class PartNumbers(db.Model):

    __tablename__ = 'arde_part_numbers'

    part_number_id = db.Column(db.String(45), primary_key=True)
    name = db.Column(db.String(45))
    alias = db.Column(db.String(45))
    arde_components_component_id = db.Column(db.String(45))


class PartNumbersSchema(ma.Schema):
    class Meta(object):
        fields = utils.class_attributes(PartNumbers)


PARTNUMBER_SCHEMA = PartNumbersSchema()
PARTNUMBERS_SCHEMA = PartNumbersSchema(many=True)
