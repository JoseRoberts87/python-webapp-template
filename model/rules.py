from app import db, ma

col = db.Column()
string = db.String(45)
integer = db.Integer

class Rule(db.Model):
    __table__= 'audit_rule_facts'

    audit_rule_facts_id = db.Column(db.Integer, autoincrement=True)
    arde_locations_location_id = db.Column(db.String(45))
    arde_components_component_id = db.Column(db.String(45))
    arde_data_categories_data_category_id = col(integer)
    arde_persons_person_id = db.Column(db.String(45))
    audit_rule_meta_rule_id = col(integer)


