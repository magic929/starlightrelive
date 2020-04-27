from models.config import *

class CharaModel(db.Model):
    __tablename__ = 'chara'

    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.TEXT)
    name_ruby = db.Column(db.TEXT)
    department_1 = db.Column(db.TEXT)
    department_2 = db.Column(db.TEXT)
    likes = db.Column(db.TEXT)
    dislikes = db.Column(db.TEXT)
    like_foods = db.Column(db.TEXT)
    dislike_foods = db.Column(db.TEXT)
    introduction = db.Column(db.TEXT)

def get_id(id):
    result = CharaModel.query.filter_by(id=id).first()
    return result