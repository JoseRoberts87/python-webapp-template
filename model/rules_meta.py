from app import db, ma
from common import utils

class RuleMeta(db.Model):

    __tablename__= 'audit_rule_meta'
    rule_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45))
    description = db.Column(db.String(45))
    sample_size = db.Column(db.Integer )
    status = db.Column(db.BOOLEAN)
    frequency = db.Column(db.Integer)
    sample_type = db.Column(db.String(45))
    priority_level = db.Column(db.Integer)

    # a different way to do this
    # def __repr__(self):
    #     return "<Meta(rule_id='%s', name='%s', description='%s', " \
    #            "sample_size='%s', status='%s', interval='%s', " \
    #            "sample_type='%s', priority_level'%s')>" % (
    #         self.rule_id, self.name,self.description,
    #         self.sample_size, self.status, self.interval,
    #         self.sample_type, self.priority_level)


class RuleMetaSchema(ma.Schema):
    class Meta(object):
        fields = utils.class_attributes(RuleMeta)
        # fields = ('rule_id','name','description','sample_size','status','frequency','sample_type','priority_level')


RULEMETA_SCHEMA =RuleMetaSchema()
RULESMETA_SCHEMA = RuleMetaSchema(many=True)