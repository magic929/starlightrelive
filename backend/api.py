from flask import Blueprint
from flask_restful import Api, Resource
from models.dress import get_id

api_bp = Blueprint('api', __name__, url_prefix='/api')

class Spam(Resource):
    def get(self):
        dress = get_id("1030003")
        return [{'name': dress.name, 'charaId': dress.chara_id}]


api = Api(api_bp)
api.add_resource(Spam, '/dress')