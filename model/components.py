from app import db, ma

class Components(db.Model):
    __tablename__ = 'arde_components'
    component_id = db.Column(db.String(45), primary_key=True)
    name = db.Column(db.String(45))
    type = db.Column(db.String(45))

class ComponentsSchema(ma.Schema):
    class Meta(object):
        fields = ('component_id', 'name', 'type')

COMPONENT_SCHEMA = ComponentsSchema()
COMPONENTS_SCHEMA = ComponentsSchema(many=True)
