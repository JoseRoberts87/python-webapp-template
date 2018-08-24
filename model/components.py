from app import db, ma
from common import utils

class Components(db.Model):
    __tablename__ = 'components'
    component_id = db.Column(db.String(45), primary_key=True)
    name = db.Column(db.String(45))
    type = db.Column(db.String(45))

class ComponentsSchema(ma.Schema):
    class Meta(object):
        fields = utils.class_attributes(Components)

COMPONENT_SCHEMA = ComponentsSchema()
COMPONENTS_SCHEMA = ComponentsSchema(many=True)
