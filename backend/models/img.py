from models.config import *

class TestModel(db.Model):
    __tablename__ = 'img'

    id = db.Column(db.INTEGER, primary_key=True)
    img_url = db.Column(db.TEXT)

def get_id(id):
    result = TestModel.query.filter_by(id=id).first()
    return result