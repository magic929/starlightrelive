from flask_sqlalchemy import SQLAlchemy
from common import utils
from models.config import *


class DressModel(db.Model):
    __tablename__ = 'dress'

    id = db.Column(db.TEXT, primary_key=True)
    name = db.Column(db.TEXT)
    chara_id = db.Column(db.INTEGER)
    cost = db.Column(db.INTEGER)
    base_agi = db.Column(db.INTEGER)
    base_rarity = db.Column(db.INTEGER)
    growth_board3_id = db.Column(db.TEXT)
    base_pdef = db.Column(db.INTEGER)
    delta_agi = db.Column(db.INTEGER)
    dex = db.Column(db.INTEGER)
    growth_board7_id = db.Column(db.TEXT)    
    eva = db.Column(db.INTEGER)
    growth_board1_id = db.Column(db.TEXT)
    party_skill_type = db.Column(db.INTEGER)    
    delta_pdef = db.Column(db.INTEGER)
    growth_board6_id = db.Column(db.TEXT)
    attribute_id = db.Column(db.INTEGER)
    growth_board4_id = db.Column(db.TEXT)    
    dress_episode_id = db.Column(db.TEXT)
    base_atk = db.Column(db.INTEGER)
    delta_atk = db.Column(db.INTEGER)
    auto_skill2_id = db.Column(db.TEXT)
    party_skill_id = db.Column(db.TEXT)
    auto_skill2_type = db.Column(db.INTEGER)
    delta_hp = db.Column(db.INTEGER)
    auto_skill1_id = db.Column(db.TEXT)
    command_skill1_id = db.Column(db.TEXT)
    auto_skill1_type = db.Column(db.INTEGER)
    attack_type = db.Column(db.INTEGER)
    growth_board5_id = db.Column(db.TEXT)
    command_skill2_id = db.Column(db.TEXT)
    auto_skill3_type = db.Column(db.INTEGER)
    delta_mdef = db.Column(db.INTEGER)
    auto_skill3_id = db.Column(db.TEXT)
    cri = db.Column(db.INTEGER)
    growth_board8_id = db.Column(db.TEXT)
    hit = db.Column(db.INTEGER)
    base_mdef = db.Column(db.INTEGER)
    growth_board2_id = db.Column(db.TEXT)
    growth_board9_id = db.Column(db.TEXT)
    command_skill3_id = db.Column(db.TEXT)
    published_at = db.Column(db.TEXT)
    command_unique_skill_id = db.Column(db.TEXT)
    dress_type = db.Column(db.INTEGER)
    base_hp = db.Column(db.INTEGER)
    description = db.Column(db.TEXT)
    
def get_id(id):
    dressid = DressModel.query.filter_by(id=id).first()
    return dressid

def get_all():
    dressid = DressModel.query.all()
    return dressid

def get_random_id():
    dressid = get_all()
    idx = utils.rand_index(len(dressid))
    result = []
    for i in idx:
        tmp = dressid[i]
        result.append({"id": tmp.id, "name": tmp.name, "charaId": tmp.chara_id})
    return result