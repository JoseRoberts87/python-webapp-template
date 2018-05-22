from app import db, ma
from common import utils

class Categories(db.Model):

    __tablename__ = 'arde_data_category'

    data_category_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))

class CategoriesSchema(ma.Schema):
    class Meta(object):
        fields = utils.class_attributes(Categories)

CATEGORY_SCHEMA = CategoriesSchema()
CATEGORIES_SCHEMA = CategoriesSchema(many=True)