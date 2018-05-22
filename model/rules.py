from app import db, ma
from common import utils

class Rules(db.Model):

    __table__= 'audit_rule_facts'

    audit_rule_facts_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    arde_locations_location_id = db.Column(db.String(45))
    arde_components_component_id = db.Column(db.String(45))
    arde_data_categories_data_category_id = db.Column(db.Integer)
    arde_persons_person_id = db.Column(db.String(45))
    audit_rule_meta_rule_id = db.Column(db.Integer)

class RuleShema(ma.Schema):
    class Meta(object):
        fields = utils.class_attributes(Rules)

RULE_SCHEMA = RuleShema()
RULES_SCHEMA = RuleShema(many=True)