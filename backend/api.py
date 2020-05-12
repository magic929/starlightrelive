from flask import Blueprint
from flask_restful import Api, Resource, reqparse
from models import dress
from models import chara
from models import img
from models import strength
from model import compute_level

from models import level

api_bp = Blueprint('api', __name__, url_prefix='/api')
parser = reqparse.RequestParser(trim=True)
parser.add_argument('strength', type=str, action='append')  
    
class Dress(Resource):
    def get(self):
        dresses = dress.get_random_id()
        for d in dresses:
            d['charaId'] = chara.get_id(d['charaId']).name
            d['img_url'] = img.get_id(d['id']).img_url.strip()
        return dresses

    def post(self):
        args = parser.parse_args()
        # result = args["strength"]
        strength.insert_one(args["strength"])

class Level(Resource):
    def get(self):
        result = level.get_level_card()
        print(result)
        return result   


api = Api(api_bp)
api.add_resource(Dress, '/dress')
api.add_resource(Level, '/level')